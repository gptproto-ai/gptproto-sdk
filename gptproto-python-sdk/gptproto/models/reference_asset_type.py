from enum import Enum


class ReferenceAssetType(str, Enum):
    AUDIO_URL = "audio_url"
    IMAGE_URL = "image_url"
    VIDEO_URL = "video_url"

    def __str__(self) -> str:
        return str(self.value)
