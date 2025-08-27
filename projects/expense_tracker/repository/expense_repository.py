from storage.index import Storage
from models.expense import Expense
from typing import List

class ExpenseRepository:
    def __init__(self, storage:Storage):
        self.storage = storage
        
    def _read_all(self) -> List[Expense]:
        blob = self.storage.load()
        return [Expense.from_dict(e) for e in blob.get("expenses", [])]
    
    def _write_all(self, expenses: List[Expense]) -> None:
        self.storage.save({"expenses": [e.to_dict() for e in expenses]})
        
    def next_id(self):
        expenses = self._read_all()
        return (max((e.id for e in expenses), default=0) + 1)
        
    def add(self, expense:Expense) -> Expense:
        expenses = self._read_all()
        expenses.append(expense)
        self._write_all(expenses)
        print(expenses)
        return expense
    
    def list(self) -> Expense:
        return sorted(self._read_all(), key=lambda e:(e.date, e.id))
    
    def delete(self, expense_id) -> bool:
        expenses = self._read_all()
        new_expenses = [e for e in expenses if e.id != expense_id]
        if len(new_expenses) == len(expenses):
            return False
        self._write_all(new_expenses)
        return True