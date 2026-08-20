from enum import Enum


class ImageAspectRatio(str, Enum):
    AUTO = "auto"
    RATIO_16_9 = "16:9"
    RATIO_19_5_9 = "19.5:9"
    RATIO_1_1 = "1:1"
    RATIO_1_2 = "1:2"
    RATIO_1_4 = "1:4"
    RATIO_1_8 = "1:8"
    RATIO_20_9 = "20:9"
    RATIO_21_9 = "21:9"
    RATIO_2_1 = "2:1"
    RATIO_2_3 = "2:3"
    RATIO_3_2 = "3:2"
    RATIO_3_4 = "3:4"
    RATIO_4_1 = "4:1"
    RATIO_4_3 = "4:3"
    RATIO_4_5 = "4:5"
    RATIO_5_4 = "5:4"
    RATIO_8_1 = "8:1"
    RATIO_9_16 = "9:16"
    RATIO_9_19_5 = "9:19.5"
    RATIO_9_20 = "9:20"
    RATIO_9_21 = "9:21"

    def __str__(self) -> str:
        return str(self.value)
