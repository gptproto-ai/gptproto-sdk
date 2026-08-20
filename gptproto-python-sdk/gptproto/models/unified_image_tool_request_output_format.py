from enum import Enum


class UnifiedImageToolRequestOutputFormat(str, Enum):
    JPEG = "jpeg"
    PNG = "png"
    SVG = "svg"
    WEBP = "webp"

    def __str__(self) -> str:
        return str(self.value)
