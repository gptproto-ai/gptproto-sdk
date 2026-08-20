from enum import Enum


class VideoResolution(str, Enum):
    RESOLUTION_1080P = "1080p"
    RESOLUTION_1K = "1K"
    RESOLUTION_2K = "2K"
    RESOLUTION_480P = "480p"
    RESOLUTION_4K = "4K"
    RESOLUTION_512 = "512"
    RESOLUTION_512P = "512p"
    RESOLUTION_540P = "540p"
    RESOLUTION_720P = "720p"
    RESOLUTION_768P = "768p"

    def __str__(self) -> str:
        return str(self.value)
