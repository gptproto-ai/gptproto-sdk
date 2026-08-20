from enum import Enum


class KwaivgiParametersVoiceLanguage(str, Enum):
    EN = "en"
    ZH = "zh"

    def __str__(self) -> str:
        return str(self.value)
