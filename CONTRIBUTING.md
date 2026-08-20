# Contributing

Thanks for your interest in contributing to gptproto SDK!

## The spec-driven workflow

This is a **spec-driven** monorepo. The OpenAPI spec at
`openapi/openapi.yaml` is the single source of truth for every language SDK.
Never hand-edit the generated code under `gptproto*/api/` or
`gptproto*/models/` — regenerate from the spec instead.

```
spec change  ->  regenerate SDKs  ->  update run() layer if needed  ->  commit
```

## Adding a new provider (e.g. a new video model vendor)

1. **Spec**: add the `POST /api/v3/{provider}/{model}/{scene}` endpoint and its
   request-body schema to `openapi/openapi.yaml`. Include enums, defaults, and
   required fields so the generated types carry them.
2. **Regenerate**: re-run the codegen for each SDK (commands are in each SDK's
   README).
3. **Register**: add one entry to the provider dispatch table in the hand-written
   `run()` layer of each SDK (e.g. `_PROVIDERS` in Python, the `providers` map
   in Go).
4. **Example**: add a sample call in `examples/`.
5. **Test**: run the SDK's demo to confirm the new provider serializes correctly.

## Adding a new language SDK

1. Choose an OpenAPI codegen tool for the language.
2. Generate the client into a new `gptproto-<lang>-sdk/` directory from
   `openapi/openapi.yaml`.
3. Implement a thin `run(provider, model, scene, body)` helper on top of the
   generated `create` + `get` functions. It should:
   - submit the task and return a `task_id`,
   - poll `GET /api/v3/predictions/{task_id}/result` until a terminal status,
   - return the result on success, raise on failure, raise on timeout.
4. Add `README.md`, `examples/`, and the language build file
   (`pyproject.toml` / `go.mod` / `package.json`).

## Conventions

- **Comments and docs in English.** This is a public, open-source project.
- **No internal references.** Do not leak internal class names, package paths,
  table names, or infrastructure details into the spec, code, or comments.
- **Keep the `run()` layer thin.** It should only do create → poll → classify.
  Provider-specific quirks belong in the spec (enums, defaults), not in
  hand-written branching.
- **One spec, many SDKs.** If a field changes, change the spec once and
  regenerate everywhere.

## Development setup

### Python

```bash
cd gptproto-python-sdk
python -m venv .venv && source .venv/bin/activate
pip install -e .
python examples/demo.py
```

### Go

```bash
cd gptproto-go-sdk
go run ./examples
```
