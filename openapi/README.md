# Public OpenAPI source

[`openapi.yaml`](./openapi.yaml) is the source of truth for every public
GPTProto SDK. It defines these unified endpoints:

- `POST /api/v3/videos` and `GET /api/v3/videos/{id}`
- `POST /api/v3/images`
- `POST /api/v3/audio/speech`
- `POST /api/v3/audio/voice-clone`
- `POST /api/v3/lip-sync`
- `POST /api/v3/3d`
- `POST /api/v3/images/edit`
- `GET /api/v3/tasks/result/{id}`

Edit field descriptions, enum values, defaults, required fields, and examples
here, then run `../generate.sh` followed by `../verify.sh`. Internal class names,
database details, infrastructure addresses, and private routing controls do not
belong in this public document.

Omitting `additionalProperties: false` intentionally keeps JSON requests
forward-compatible. The SDKs still expose all documented fields and enums as
strong types.
