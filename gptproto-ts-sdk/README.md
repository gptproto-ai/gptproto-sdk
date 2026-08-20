# GPTProto TypeScript SDK

Typed client for the GPTProto unified asynchronous media API. Models and HTTP
services are generated from `../openapi/openapi.yaml`; `src/client.ts` adds the
hand-written `create`, `get`, and `run` helpers.

## Use

```bash
npm install
npm run build
export GPTPROTO_API_KEY=your_key
```

```ts
import { GptprotoClient, VideoResolution } from 'gptproto';

const client = new GptprotoClient();
const result = await client.run('video', {
  model: 'kling/kling-v3.0-pro',
  prompt: 'a cat dancing',
  duration: 5,
  resolution: VideoResolution.RESOLUTION_1080P,
});
console.log(result.unsigned_urls);
```

Task kinds are `video`, `image`, `speech`, `voice-clone`, `lip-sync`, `3d`,
and `image-tool`. `run()` polls until `completed` or throws on `failed`,
`cancelled`, `expired`, or timeout. Use `create()` and `get()` for manual
polling.

## Develop

```bash
npm run generate
npm run typecheck
npm run build
npm run dev
```

Run the repository-level `../generate.sh` when all language SDKs must stay in
sync.
