"""Exercise the public Python SDK against a local gateway without submitting a channel task."""

import os

from gptproto import GptprotoClient
from gptproto.models import UnifiedVideoRequest


base_url = os.environ["GPTPROTO_SDK_TEST_BASE_URL"]
client = GptprotoClient(base_url=base_url)

try:
    client.create(
        "video",
        UnifiedVideoRequest(
            model="sdk-test/not-a-real-model",
            prompt="SDK contract probe",
        ),
    )
except RuntimeError as exc:
    if "code=400" not in str(exc):
        raise
    print("Python gateway contract: ok")
else:
    raise RuntimeError("expected the local gateway to reject the probe model")
