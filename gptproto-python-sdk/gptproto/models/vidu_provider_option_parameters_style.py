from enum import Enum


class ViduProviderOptionParametersStyle(str, Enum):
    ANIME = "anime"
    GENERAL = "general"

    def __str__(self) -> str:
        return str(self.value)
