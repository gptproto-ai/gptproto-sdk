"""Hand-written create/poll helpers on top of the generated unified client."""
import os
import time
from typing import Callable, Literal, Optional, Union

from .api.audio import create_speech, create_voice_clone
from .api.extensions import create_3d, create_image_tool, create_lip_sync
from .api.image import create_image
from .api.tasks import get_task, get_video_task
from .api.video import create_video
from .client import AuthenticatedClient
from .models.unified_3d_request import Unified3DRequest
from .models.unified_error_response import UnifiedErrorResponse
from .models.unified_image_request import UnifiedImageRequest
from .models.unified_image_tool_request import UnifiedImageToolRequest
from .models.unified_lip_sync_request import UnifiedLipSyncRequest
from .models.unified_speech_request import UnifiedSpeechRequest
from .models.unified_task_result import UnifiedTaskResult
from .models.unified_voice_clone_request import UnifiedVoiceCloneRequest
from .models.unified_video_request import UnifiedVideoRequest
from .types import UNSET, Unset

TaskKind = Literal[
    "video", "image", "speech", "voice-clone", "lip-sync", "3d", "image-tool"
]
UnifiedCreateRequest = Union[
    UnifiedVideoRequest,
    UnifiedImageRequest,
    UnifiedSpeechRequest,
    UnifiedVoiceCloneRequest,
    UnifiedLipSyncRequest,
    Unified3DRequest,
    UnifiedImageToolRequest,
]

_SUCCESS = {"completed"}
_FAILED = {"failed", "cancelled", "expired"}


class TaskFailedError(Exception):
    def __init__(self, task_id: str, status: str, error: str):
        self.task_id = task_id
        self.status = status
        self.error = error
        super().__init__(f"task {task_id} ended with {status}: {error}")


class TaskTimeoutError(Exception):
    def __init__(self, task_id: str):
        self.task_id = task_id
        super().__init__(f"task {task_id} polling timeout")


_CREATORS = {
    "video": create_video,
    "image": create_image,
    "speech": create_speech,
    "voice-clone": create_voice_clone,
    "lip-sync": create_lip_sync,
    "3d": create_3d,
    "image-tool": create_image_tool,
}


class GptprotoClient:
    """GPTProto unified async media client."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://gptproto.com",
        timeout: float = 30.0,
    ):
        token = api_key or os.environ.get("GPTPROTO_API_KEY")
        if not token:
            raise ValueError("Missing API key: pass api_key= or set GPTPROTO_API_KEY")
        self._client = AuthenticatedClient(
            base_url=base_url, token=token, timeout=timeout
        )

    def create(
        self, kind: TaskKind, body: UnifiedCreateRequest
    ) -> UnifiedTaskResult:
        """Submit one task through the unified endpoint selected by kind."""
        creator = _CREATORS[kind]
        result = creator.sync(client=self._client, body=body)
        return self._expect_task_result(result)

    def get(self, task_id: str, kind: TaskKind = "video") -> UnifiedTaskResult:
        """Query once; video and non-video tasks use their canonical URLs."""
        query = get_video_task if kind == "video" else get_task
        result = query.sync(id=task_id, client=self._client)
        return self._expect_task_result(result)

    def run(
        self,
        kind: TaskKind,
        body: UnifiedCreateRequest,
        timeout: float = 600.0,
        poll_interval: float = 3.0,
        on_status: Optional[Callable[[str, str], None]] = None,
    ) -> UnifiedTaskResult:
        """Submit and poll until the task reaches a terminal unified status."""
        created = self.create(kind, body)
        deadline = time.time() + timeout
        while time.time() < deadline:
            result = self.get(created.id, kind)
            status = result.status.value
            if on_status:
                on_status(created.id, status)
            if status in _SUCCESS:
                return result
            if status in _FAILED:
                error = result.error if not isinstance(result.error, Unset) else "unknown"
                raise TaskFailedError(created.id, status, error)
            time.sleep(poll_interval)
        raise TaskTimeoutError(created.id)

    @staticmethod
    def _expect_task_result(
        result: UnifiedTaskResult | UnifiedErrorResponse | None,
    ) -> UnifiedTaskResult:
        if isinstance(result, UnifiedTaskResult):
            return result
        if isinstance(result, UnifiedErrorResponse):
            code = result.error.code
            message = result.error.message
            raise RuntimeError(f"request rejected: code={code} message={message}")
        raise RuntimeError(f"unexpected empty response: {result}")
