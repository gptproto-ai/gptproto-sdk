"""Exercise every public Python SDK route against the loopback transport mock."""
import os

from gptproto import GptprotoClient
from gptproto.models import (
    Unified3DRequest,
    UnifiedImageRequest,
    UnifiedImageToolRequest,
    UnifiedLipSyncRequest,
    UnifiedSpeechRequest,
    UnifiedVideoRequest,
    UnifiedVoiceCloneRequest,
)

client = GptprotoClient(base_url=os.environ["GPTPROTO_SDK_TEST_BASE_URL"])
requests = [
    ("video", UnifiedVideoRequest(model="test/video", prompt="test")),
    ("image", UnifiedImageRequest(model="test/image", prompt="test")),
    ("speech", UnifiedSpeechRequest(model="test/speech", input_="test", voice="test")),
    ("voice-clone", UnifiedVoiceCloneRequest(model="test/voice-clone", audio="https://example.invalid/audio.mp3")),
    ("lip-sync", UnifiedLipSyncRequest(model="test/lip-sync", video="https://example.invalid/video.mp4", audio="https://example.invalid/audio.mp3")),
    ("3d", Unified3DRequest(model="test/3d", image="https://example.invalid/image.png")),
    ("image-tool", UnifiedImageToolRequest(model="test/image-tool", image="https://example.invalid/image.png")),
]
for kind, body in requests:
    created = client.create(kind, body)
    assert created.status.value == "pending" and created.id.startswith("local-"), kind
for kind in ("video", "image"):
    assert client.get("local-check", kind).status.value == "completed", kind
assert client.run("video", UnifiedVideoRequest(model="test/video", prompt="test"), timeout=1, poll_interval=0.001).status.value == "completed"
print("Python local transport contract: ok")
