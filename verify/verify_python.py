"""End-to-end verification of the published gptproto Python SDK against the live API.

Usage:
    export GPTPROTO_API_KEY=your_key
    python verify_python.py
"""
import os
import sys

from gptproto import GptprotoClient, TaskFailedError
from gptproto.models import UnifiedImageRequest, UnifiedVideoRequest

API_KEY = os.environ.get("GPTPROTO_API_KEY")
BASE_URL = os.environ.get("GPTPROTO_BASE_URL", "https://gptproto.com")


def main() -> int:
    if not API_KEY:
        print("Missing API key - please `export GPTPROTO_API_KEY=your_key` first")
        return 1

    client = GptprotoClient(api_key=API_KEY, base_url=BASE_URL)

    # ---- Test 1: video task (create + get) ----
    print("=== Test 1: video task (create + get) ===")
    video_req = UnifiedVideoRequest(
        model="kling/kling-v3.0-pro",
        prompt="a cat dancing",
        duration=5,
    )
    created = client.create("video", video_req)
    print(f"  created  taskId={created.id}  status={created.status.value}")

    result = client.get(created.id, "video")
    print(f"  fetched  taskId={result.id}  status={result.status.value}")

    # ---- Test 2: image task (create + get) ----
    print("=== Test 2: image task (create + get) ===")
    image_req = UnifiedImageRequest(
        model="bytedance/doubao-seedream-4-5-251128",
        prompt="a red apple on a table",
    )
    img_created = client.create("image", image_req)
    print(f"  created  taskId={img_created.id}  status={img_created.status.value}")

    img_result = client.get(img_created.id, "image")
    print(f"  fetched  taskId={img_result.id}  status={img_result.status.value}")

    # ---- Test 3 (optional): full run() polling to terminal state ----
    if os.environ.get("RUN_FULL", "") == "1":
        print("=== Test 3: full run() polling (slow, will incur cost) ===")
        full = client.run(
            "video",
            UnifiedVideoRequest(model="kling/kling-v3.0-pro", prompt="a cat dancing", duration=5),
            timeout=300,
            poll_interval=5,
            on_status=lambda tid, st: print(f"    [{tid[:8]}] {st}"),
        )
        print(f"  done  status={full.status.value}  unsigned_urls={full.unsigned_urls}")

    print("\nAll verification checks passed")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except TaskFailedError as e:
        print(f"Task failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Verification failed: {type(e).__name__}: {e}")
        sys.exit(1)