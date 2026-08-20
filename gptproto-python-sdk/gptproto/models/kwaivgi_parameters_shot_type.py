from enum import Enum


class KwaivgiParametersShotType(str, Enum):
    CUSTOMIZE = "customize"
    INTELLIGENCE = "intelligence"

    def __str__(self) -> str:
        return str(self.value)
