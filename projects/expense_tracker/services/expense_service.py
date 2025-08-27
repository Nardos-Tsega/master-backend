from repository.expense_repository import ExpenseRepository
from models.expense import Expense
from typing import List, Optional
from pathlib import Path
from datetime import date
import csv

class ExpenseService:
    def __init__(self, repo:ExpenseRepository):
        self.repo = repo
        
    def add_expense(self, description:str, amount: float) -> Expense:
        new = Expense(
            id=self.repo.next_id(),
            description=description,
            amount=round(float(amount), 2),
            date=date.today().isoformat()
        )
        return self.repo.add(new)
    
    def list_expenses(self) -> List[Expense]:
        return self.repo.list()
    
    def delete_expense(self, expense_id:int) -> bool:
        return self.repo.delete(expense_id)
    
    def total(self, month: Optional[int] = None) -> float:
        expenses = self.repo.list()
        def matches(e:Expense) -> bool:
            if month is None:
                return True
            m, _ = map(int, e.date.split("-"))
            if month is not None and m != month:
                return False
            return True
        return round(sum(e.amount for e in expenses if matches(e)), 2)
    
    def export_csv(self, path:Path) -> Path:
        expenses = self.repo.list()
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "DATE", "DESCRIPTION", "AMOUNT"])
            for e in expenses:
                writer.writerow([e.id, e.date, e.description, f"{e.amount:.2f}"])
            return path