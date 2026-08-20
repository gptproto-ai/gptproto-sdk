# GPTProto SDK

Public, spec-driven SDKs for the [GPTProto](https://gptproto.com) unified asynchronous media API.

The API uses stable resource endpoints such as `POST /api/v3/videos` and puts
the provider/model slug in `model`, for example `kling/kling-v3.0-pro`. Common
fields use a unified naming scheme; capabilities unique to GPTProto remain
additive fields or provider options.

## Repository layout

```text
openapi/openapi.yaml       Public source of truth
docs/API.md                Public API reference (auth, endpoints, polling, status)
gptproto-ts-sdk/           TypeScript package
gptproto-python-sdk/       Python package
gptproto-go-sdk/           Go module
generate.sh                Regenerate typed code only
verify.sh                  Lint, build, install, and test all SDKs
```

Each language keeps generated models/transport separate from its small
hand-written `create`/`get`/`run` polling layer, so regeneration does not erase
SDK ergonomics.

## TypeScript

```ts
import { GptprotoClient } from 'gptproto';

const client = new GptprotoClient(); // GPTPROTO_API_KEY
const result = await client.run('video', {
  model: 'kling/kling-v3.0-pro',
  prompt: 'a cat dancing',
  duration: 5,
});
console.log(result.unsigned_urls);
```

## Python

```python
from gptproto import GptprotoClient
from gptproto.models import UnifiedVideoRequest

client = GptprotoClient()  # GPTPROTO_API_KEY
result = client.run(
    "video",
    UnifiedVideoRequest(
        model="kling/kling-v3.0-pro",
        prompt="a cat dancing",
        duration=5,
    ),
)
print(result.unsigned_urls)
```

## Go

```go
client := gptproto.NewClient("") // GPTPROTO_API_KEY
request := gptproto.NewUnifiedVideoRequest("kling/kling-v3.0-pro", "a cat dancing")
request.SetDuration(5)
result, err := client.Run(ctx, gptproto.TaskKindVideo, request, nil)
```

## Development

```bash
./generate.sh  # regenerate from openapi/openapi.yaml; no publishing
./verify.sh    # validate the spec and all three SDKs; no network API call
./local-contract-test.sh  # test all SDKs against a loopback test gateway
./local-transport-test.sh # test create/get/run across every SDK route, loopback only
```

`local-contract-test.sh` refuses non-loopback URLs and deliberately submits an
unknown model. It verifies SDK authentication, request serialization, endpoint
routing, and unified error decoding without creating a provider task.

`local-transport-test.sh` starts its own loopback mock and verifies successful
`create`, `get`, and `run` behavior for all seven create endpoints in all three
SDKs. It never contacts a GPTProto environment or a provider channel.

The OpenAPI Generator version (`6.6.0`) is only the Go code-generation tool
version. The public HTTP interface remains `/api/v3`.

## License

[MIT](./LICENSE)
