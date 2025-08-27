import argparse
from pathlib import Path
from services.expense_service import ExpenseService
from storage.json_storage import JSONStorage
from repository.expense_repository import ExpenseRepository
from cli.cli import cmd_add, cmd_delete, cmd_list, cmd_summary, cmd_export

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="expense-tracker-cli",
        description="Track your expenses"
    )
    
    sub = p.add_subparsers(dest="command", required=True)
    
    #add
    sp_add = sub.add_parser("add")
    sp_add.add_argument("--description", required=True)
    sp_add.add_argument("--amount", required=True)
    sp_add.set_defaults(func=cmd_add)
    
    #list
    sp_list = sub.add_parser("list")
    sp_list.set_defaults(func=cmd_list)
    
    #summary
    sp_sum = sub.add_parser("summary")
    sp_sum.add_argument("--month", type=int)
    sp_sum.set_defaults(func=cmd_summary)
    
    #delete
    sp_del = sub.add_parser("delete")
    sp_del.add_argument("--id", type=int, required=True)
    sp_del.set_defaults(func=cmd_delete)
    
    #export
    sp_export = sub.add_parser("export")
    sp_export.add_argument("--csv", required=True)
    sp_export.set_defaults(func=cmd_export)
    
    return p
    
def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    
if __name__ == "__main__":
    main()