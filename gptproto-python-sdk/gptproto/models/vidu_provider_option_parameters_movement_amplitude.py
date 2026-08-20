from enum import Enum


class ViduProviderOptionParametersMovementAmplitude(str, Enum):
    AUTO = "auto"
    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"

    def __str__(self) -> str:
        return str(self.value)
