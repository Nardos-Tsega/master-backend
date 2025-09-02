from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class Expense:
    id: int
    date: str
    description: str
    amount: int
    
    def to_dict(self):
        return asdict(self)
    
    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Expense(
            id=int(d["id"]),
            description=str(d["description"]),
            amount=float(d["amount"]),
            date=str(d["date"])
        )