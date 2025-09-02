from pathlib import Path
from storage.json_storage import JSONStorage
from services.expense_service import ExpenseService
from repository.expense_repository import ExpenseRepository


DEFAULT_DB = Path.home()/".expense_tracker"/"db.json"

def make_service(db_path:Path = DEFAULT_DB) -> ExpenseService:
    storage = JSONStorage(db_path)
    repo = ExpenseRepository(storage)
    return ExpenseService(repo)

def cmd_add(args):
    service = make_service()
    exp = service.add_expense(description=args.description, amount=args.amount)
    print(f"Expense added successfully (ID: {exp.id})")

def cmd_list(args):
    service = make_service()
    items = service.list_expenses()
    print("ID  Date        Description  Amount")
    for e in items:
        amt = f"${int(e.amount) if e.amount.is_integer() else e.amount}"
        print(f"{e.id:<3} {e.date:<10}  {e.description:<12} {amt}")


def cmd_summary(args):
    service = make_service()
    total = service.total(month=args.month)
    if args.month:
        print(f"Total expenses for {args.year}-{args.month:02d}: ${total}")
    elif args.month:
        print(f"Total expenses for month {args.month}: ${total}")
    else:
        print(f"Total expenses: ${total}")

def cmd_delete(args):
    service = make_service()
    ok = service.delete_expense(args.id)
    if ok:
        print("Expense deleted successfully")
    else:
        print("No expense found with that ID")
    
def cmd_export(args):
    service = make_service()
    out = Path(args.csv).expanduser()
    service.export_csv(out)
    print(f"Exported to CSV: {out}")