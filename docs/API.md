# gptproto API Reference

Public API reference for the [gptproto](https://gptproto.com) unified
asynchronous media generation API.

gptproto exposes **one endpoint per modality** (video, image, audio, 3D,
lip-sync, image tools). You switch models by changing the `model` field, not
the endpoint. Every generation endpoint is asynchronous: submit a task, then
poll for the result.

This reference is split into two parts: **Part 1** covers the unified flow that
every endpoint shares (auth, routing, polling, status, errors, passthrough).
**Part 2** documents each endpoint's request fields, enums, and per-provider
support in detail.

---

# Part 1 — Unified API flow

## 1.1 Authentication

All requests require an API key in the `Authorization` header:

```
Authorization: Bearer <GPTPROTO_API_KEY>
```

Get an API key from <https://gptproto.com/dashboard/api-key>. Keep it secret —
treat it like a password.

```bash
curl -X POST https://gptproto.com/api/v3/videos \
  -H "Authorization: Bearer $GPTPROTO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"kling/kling-v3.0-pro","prompt":"a cat dancing"}'
```

A missing or invalid key returns `401` with a unified error body (see §1.6).

## 1.2 Endpoint overview

One endpoint per modality. All generation endpoints are **asynchronous**.

| Modality | Method & path | Mode |
|----------|---------------|------|
| Video generation | `POST /api/v3/videos` | async (submit + poll) |
| Image generation | `POST /api/v3/images` | async (submit + poll) |
| Text-to-speech | `POST /api/v3/audio/speech` | async (submit + poll) |
| Voice cloning | `POST /api/v3/audio/voice-clone` | async (submit + poll) |
| Lip sync | `POST /api/v3/lip-sync` | async (submit + poll) |
| 3D generation | `POST /api/v3/3d` | async (submit + poll) |
| Image tools (upscale/watermark) | `POST /api/v3/images/edit` | async (submit + poll) |
| Task result (poll) | `GET /api/v3/tasks/result/{id}` | query |

There is also `GET /api/v3/videos/{id}` as an alias of the task-result
endpoint for video tasks.

## 1.3 Model routing

The `model` field uses `provider/model` slug format:

```json
{ "model": "kling/kling-v3.0-pro" }
```

- `provider` is the vendor (e.g. `kling`, `google`, `bytedance`, `alibaba`,
  `minimax`, `vidu`, `openai`, `midjourney`).
- `model` is the vendor's model name.

To use a different model you only change the `model` string — the endpoint and
the rest of the request shape stay the same.

## 1.4 Asynchronous flow (create → poll)

Every generation endpoint follows the same two-step flow.

**Step 1 — submit.** `POST` the create endpoint. You get `202 Accepted` with a
task id and `status: "pending"`:

```json
{
  "id": "job-abc123",
  "generation_id": "gen-xyz789",
  "polling_url": "/api/v3/tasks/result/job-abc123",
  "status": "pending"
}
```

**Step 2 — poll.** `GET` the task-result endpoint until `status` reaches a
terminal value:

```json
{
  "id": "job-abc123",
  "status": "completed",
  "unsigned_urls": ["https://.../result.mp4"],
  "native_status": "completed"
}
```

- `completed` → the result is in `unsigned_urls`.
- `failed` / `cancelled` / `expired` → check the `error` field.
- `pending` / `in_progress` → keep polling (suggest 3–5s between requests).

> `202` on submit means "accepted, not finished yet" — this is normal for an
> async task. `200` on poll means the result is returned.

## 1.5 Status enum

The unified `status` field uses exactly six values:

| Value | Meaning |
|-------|---------|
| `pending` | task accepted, queued |
| `in_progress` | task is being generated |
| `completed` | generation succeeded, result in `unsigned_urls` |
| `failed` | generation failed, see `error` |
| `cancelled` | task was cancelled |
| `expired` | task expired before completion |

`native_status` preserves the upstream provider's raw status string, so you can
still inspect the original value while relying on the unified `status` field for
decision-making.

## 1.6 Errors

Errors use a consistent JSON shape:

```json
{
  "code": 401,
  "message": "Token cannot be empty",
  "type": "error"
}
```

| HTTP | Typical cause |
|------|---------------|
| `400` | invalid request (missing/invalid fields) |
| `401` | missing or invalid API key |
| `429` | upstream provider error or channel unavailable |
| `5xx` | internal / upstream failure |

## 1.7 Provider passthrough

Fields that are specific to a single provider (not part of the unified schema)
go under `provider.options`, keyed by provider slug:

```json
{
  "model": "kling/kling-v3.0-pro",
  "prompt": "a cat dancing",
  "provider": {
    "options": {
      "kling": { "parameters": { "voice_id": "AOT" } }
    }
  }
}
```

Unified fields a provider does not support are ignored silently.

## 1.8 Nested structures

### `frame_images` (video)

```json
[
  { "type": "image_url", "image_url": { "url": "https://..." }, "frame_type": "first_frame" }
]
```

- `type`: always `"image_url"`
- `image_url.url`: the image URL
- `frame_type`: `"first_frame"` | `"last_frame"`

### `input_references` (video / image)

```json
[
  { "type": "image_url", "image_url": { "url": "https://..." } },
  { "type": "video_url", "image_url": { "url": "https://..." } },
  { "type": "audio_url", "image_url": { "url": "https://..." } }
]
```

- `type`: `"image_url"` | `"video_url"` | `"audio_url"`
- `image_url.url`: the asset URL (the field is named `image_url` for all asset
  kinds)

### `provider` (all endpoints)

```json
{ "options": { "kling": { "parameters": { "voice_id": "AOT" } } } }
```

Provider-specific parameters go under `options[slug].parameters`. gptproto
passes them through untouched.

---

# Part 2 — Endpoint reference

## 2.1 Video generation — `POST /api/v3/videos`

### Request fields

| Field | Type | Required | Supported by |
|-------|------|----------|--------------|
| `model` | string | ✅ | all |
| `prompt` | string | — | all |
| `mode` | string | — | all (scene override) |
| `duration` | integer | — | kling, vidu, seedance, wan, hailuo, sora |
| `resolution` | enum | — | kling, veo, vidu, seedance, wan, hailuo, sora |
| `aspect_ratio` | enum | — | kling, veo, vidu, seedance |
| `size` | string | — | vidu, wan, sora, grok |
| `frame_images` | array | — | all (wan, sora, grok: first_frame only) |
| `input_references` | array | — | all |
| `generate_audio` | boolean | — | kling (sound), vidu (audio), seedance (generate_audio) |
| `seed` | integer | — | vidu, seedance, wan |
| `negative_prompt` | string | — | kling, vidu, wan |
| `provider` | object | — | all (§1.7) |

### Enums

`resolution`:

| Value | Supported by |
|-------|--------------|
| `480p` | kling |
| `720p` | kling, veo, vidu, seedance, wan, hailuo, sora |
| `1080p` | kling, veo, vidu, hailuo, sora |
| `540p` | hailuo |
| `512`, `720`, `1080` | vidu |
| `512p`, `768p`, `1K`, `2K`, `4K` | — |

`aspect_ratio`:

| Value | Supported by |
|-------|--------------|
| `16:9` | kling, veo, vidu, seedance |
| `9:16` | kling, veo, vidu, seedance |
| `1:1` | kling |
| `auto` | vidu |
| `4:3`, `3:4`, `3:2`, `2:3`, `21:9`, `9:21` | — |

### Support matrix

| Provider | duration | aspect_ratio | first_frame | last_frame | reference | seed | negative_prompt | audio |
|----------|----------|--------------|-------------|------------|-----------|------|-----------------|-------|
| `kling` | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | sound |
| `veo` | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| `vidu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | audio |
| `seedance` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | generate_audio |
| `wan` | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ |
| `hailuo` | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| `sora` | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| `grok` | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

> ✅ = supported; ❌ = ignored by that provider.

### Scene inference

- `frame_images` with `first_frame` → `image-to-video`
- `input_references` with a video/image asset → `reference-to-video`
- otherwise → `text-to-video`
- `mode` overrides the inference when set.

## 2.2 Image generation — `POST /api/v3/images`

### Request fields

| Field | Type | Required | Supported by |
|-------|------|----------|--------------|
| `model` | string | ✅ | all |
| `prompt` | string | — | all |
| `aspect_ratio` | enum | — | google, vidu |
| `resolution` | enum | — | vidu, wan (seedream, google: as size fallback) |
| `size` | string | — | seedream, google, openai, qwen, wan, novel |
| `n` | integer | — | seedream, openai, wan, vidu, novel |
| `quality` | enum | — | openai |
| `output_format` | enum | — | openai, google, qwen |
| `background` | enum | — | openai |
| `seed` | integer | — | qwen, wan, vidu, novel |
| `input_references` | array | — | all |
| `provider` | object | — | all (§1.7) |

### Enums

`resolution`:

| Value | Supported by |
|-------|--------------|
| `512` | vidu |
| `1K`, `2K`, `4K` | — |

`aspect_ratio`:

| Value | Supported by |
|-------|--------------|
| `1:1`, `1:2`, `1:4`, `1:8`, `2:1`, `2:3`, `3:2`, `3:4`, `4:1`, `4:3`, `4:5`, `5:4`, `8:1`, `9:16`, `16:9`, `9:19.5`, `19.5:9`, `9:20`, `20:9`, `9:21`, `21:9`, `auto` | google, vidu |

`quality`:

| Value | Supported by |
|-------|--------------|
| `auto`, `low`, `medium`, `high` | openai |

`output_format`:

| Value | Supported by |
|-------|--------------|
| `png`, `jpeg` | google, openai, qwen |
| `webp`, `svg` | openai, qwen |

`background`:

| Value | Supported by |
|-------|--------------|
| `auto`, `transparent`, `opaque` | openai |

### Support matrix

| Provider | resolution/size | aspect_ratio | n | seed | image-to-image | mask/edit | vendor-specific (via `provider.options`) |
|----------|-----------------|--------------|---|------|----------------|-----------|------------------------------------------|
| `seedream` | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | enable_sync_mode |
| `midjourney` | ❌ (photoUri) | ❌ | ❌ | ❌ | ✅ | ❌ | state, botType |
| `google` | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | temperature, topP, topK |
| `openai` | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | quality, background |
| `qwen` | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | loras |
| `wan` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | mode |
| `vidu` | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | style, template |
| `novel` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | steps, scale, sampler, controlnet |

### Scene inference

- `input_references` present → `image-to-image`
- `input_references` empty → `text-to-image`

> **Vendor exceptions**: `vidu` → `reference-to-image`; `google` → `image-edit`;
> `openai` → `image-edit` when a `mask` is supplied.

## 2.3 Audio

### Text-to-speech — `POST /api/v3/audio/speech`

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `model` | string | ✅ | TTS model slug |
| `input` | string | ✅ | Text to synthesize |
| `voice` | string | ✅ | Voice id |
| `speed` | number | — | Playback speed |
| `provider` | object | — | Passthrough |

### Voice clone — `POST /api/v3/audio/voice-clone`

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `model` | string | ✅ | Voice-clone model slug |
| `audio` | string | ✅ | Source audio URL |
| `text` | string | — | Text to speak |
| `custom_voice_id` | string | — | Reuse an existing cloned voice |
| `accuracy` | number | — | Clone fidelity |
| `need_noise_reduction` | boolean | — | Denoise input |
| `need_volume_normalization` | boolean | — | Normalize volume |
| `provider` | object | — | Passthrough |

### Lip sync — `POST /api/v3/lip-sync`

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `model` | string | ✅ | Lip-sync model slug |
| `video` | string | ✅ | Video URL |
| `audio` | string | ✅ | Audio URL |
| `provider` | object | — | Passthrough |

## 2.4 3D generation — `POST /api/v3/3d`

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `model` | string | ✅ | 3D model slug |
| `mode` | string | — | Generation mode |
| `image` | string | — | Single reference image |
| `front_image_url` / `back_image_url` / `left_image_url` / `right_image_url` | string | — | Multi-view reference images |
| `provider` | object | — | Passthrough |

## 2.5 Image tools — `POST /api/v3/images/edit`

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `model` | string | ✅ | Tool model slug |
| `mode` | string | — | Tool mode |
| `image` | string | — | Input image URL |
| `video` | string | — | Input video URL |
| `creativity` | number | — | Creativity strength |
| `target_resolution` | string | — | Upscale target |
| `size` | string | — | Output size |
| `output_format` | string | — | Output format |
| `enable_base64_output` | boolean | — | Return base64 |
| `enable_sync_mode` | boolean | — | Synchronous mode |
| `provider` | object | — | Passthrough |
