from enum import Enum


class ImageResolution(str, Enum):
    RESOLUTION_1K = "1K"
    RESOLUTION_2K = "2K"
    RESOLUTION_4K = "4K"
    RESOLUTION_512 = "512"

    def __str__(self) -> str:
        return str(self.value)
