"""Build a typed request without making a network call."""

from gptproto.models import UnifiedVideoRequest


request = UnifiedVideoRequest(
    model="kling/kling-v3.0-pro",
    prompt="a cat dancing",
    duration=5,
)
print(request.to_dict())

# Live example (requires GPTPROTO_API_KEY):
# from gptproto import GptprotoClient
# result = GptprotoClient().run("video", request)
# print(result.unsigned_urls)
