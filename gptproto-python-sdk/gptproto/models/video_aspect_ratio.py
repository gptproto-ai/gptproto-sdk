from enum import Enum


class VideoAspectRatio(str, Enum):
    AUTO = "auto"
    LANDSCAPE_16_9 = "16:9"
    LANDSCAPE_3_2 = "3:2"
    LANDSCAPE_4_3 = "4:3"
    PORTRAIT_2_3 = "2:3"
    PORTRAIT_3_4 = "3:4"
    PORTRAIT_9_16 = "9:16"
    SQUARE_1_1 = "1:1"
    TALL_9_21 = "9:21"
    ULTRAWIDE_21_9 = "21:9"

    def __str__(self) -> str:
        return str(self.value)
