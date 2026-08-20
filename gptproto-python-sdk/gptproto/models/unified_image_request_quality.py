from enum import Enum


class UnifiedImageRequestQuality(str, Enum):
    AUTO = "auto"
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"

    def __str__(self) -> str:
        return str(self.value)
