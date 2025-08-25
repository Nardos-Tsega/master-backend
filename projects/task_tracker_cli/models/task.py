import datetime
from dataclasses import dataclass, field
from enum import Enum
import uuid

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    
class Status(Enum):
    IN_PROGRESS = 1
    DONE = 2
    CANCELLED = 3

@dataclass(frozen=True)
class TaskId:
    value: str

    @staticmethod
    def new() -> "TaskId":
        """Factory for new unique TaskId."""
        return TaskId(str(uuid.uuid4()))

@dataclass
class Task:
    id: TaskId
    title: str
    created_at: datetime.datetime = field(default_factory=datetime.datetime.utcnow)
    priority: Priority = Priority.MEDIUM
    status: Status = Status.IN_PROGRESS
    
    def to_dict(self):
        return {
            "id": self.id.value,
            "title": self.title,
            "created_at": self.created_at.isoformat(),
            "priority": self.priority.name,
            "status": self.status.name,
        }

    @staticmethod
    def from_dict(d: dict) -> "Task":
        return Task(
            id=TaskId(d["id"]),
            title=d["title"],
            created_at=datetime.datetime.fromisoformat(d["created_at"]),
            priority=Priority[d["priority"]],
            status=Status[d["status"]],
        )