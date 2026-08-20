from enum import Enum


class UnifiedTaskResultStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    EXPIRED = "expired"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
