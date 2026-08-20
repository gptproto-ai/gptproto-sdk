from enum import Enum


class SoraReverseProviderOptionParametersOrientation(str, Enum):
    LANDSCAPE = "landscape"
    PORTRAIT = "portrait"

    def __str__(self) -> str:
        return str(self.value)
