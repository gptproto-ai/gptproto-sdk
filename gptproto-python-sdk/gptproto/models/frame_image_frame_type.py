from enum import Enum


class FrameImageFrameType(str, Enum):
    FIRST_FRAME = "first_frame"
    LAST_FRAME = "last_frame"

    def __str__(self) -> str:
        return str(self.value)
