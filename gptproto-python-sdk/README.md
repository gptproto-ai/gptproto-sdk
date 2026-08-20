# GPTProto Python SDK

Typed Python client for the GPTProto unified asynchronous media API. The
generated transport and models are wrapped by `GptprotoClient` for unified
create/get/run polling.

## Use

```bash
pip install gptproto
export GPTPROTO_API_KEY=your_key
```

```python
from gptproto import GptprotoClient
from gptproto.models import UnifiedVideoRequest, VideoResolution

client = GptprotoClient()
result = client.run(
    "video",
    UnifiedVideoRequest(
        model="kling/kling-v3.0-pro",
        prompt="a cat dancing",
        duration=5,
        resolution=VideoResolution.RESOLUTION_1080P,
    ),
)
print(result.unsigned_urls)
```

Task kinds are `video`, `image`, `speech`, `voice-clone`, `lip-sync`, `3d`,
and `image-tool`. `run()` returns on `completed`, raises `TaskFailedError` for
`failed`, `cancelled`, or `expired`, and raises `TaskTimeoutError` on timeout.

For local development:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .
python examples/demo.py
```

Use the repository-level `../generate.sh` to regenerate without overwriting
the hand-written `run.py` and public `__init__.py`.
