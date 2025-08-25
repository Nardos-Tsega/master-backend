import sys
import argparse
from datetime import datetime
from models.task import Priority, Status
from repos.json_repo import JsonTaskRepo
from services.task_service import TaskService

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="Simple Todo CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="Task title")
    p_add.add_argument("--priority", choices=[p.name for p in Priority],
                       default="MEDIUM", help="Priority (default: MEDIUM)")

    # list
    p_list = sub.add_parser("list", help="List all tasks")

    # get
    p_get = sub.add_parser("get", help="Show one task")
    p_get.add_argument("id", help="Task ID")

    # status
    p_status = sub.add_parser("status", help="Update task status")
    p_status.add_argument("id", help="Task ID")
    p_status.add_argument("status", choices=[s.name for s in Status],
                          help="New status")

    # priority
    p_pri = sub.add_parser("priority", help="Update task priority")
    p_pri.add_argument("id", help="Task ID")
    p_pri.add_argument("priority", choices=[p.name for p in Priority],
                       help="New priority")

    # remove
    p_rm = sub.add_parser("remove", help="Delete a task")
    p_rm.add_argument("id", help="Task ID")

    return parser

def fmt_dt(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def print_task(t) -> None:
    mark = {Status.DONE: "✓", Status.CANCELLED: "✗"}.get(t.status, "•")
    print(f"{mark} {t.id.value} | {t.title} | {t.priority.name} | {t.status.name} | {fmt_dt(t.created_at)}")

def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    repo = JsonTaskRepo("tasks.json")
    svc = TaskService(repo)

    if args.command == "add":
        t = svc.add(args.title, priority=Priority[args.priority])
        print(f"Added: {t.id.value}  ({t.priority.name})")
        return 0

    if args.command == "list":
        tasks = svc.list()
        if not tasks:
            print("No tasks yet.")
            return 0
        for t in tasks:
            print_task(t)
        return 0

    if args.command == "get":
        t = svc.get(args.id)
        if not t:
            print("Not found")
            return 1
        print_task(t)
        return 0

    if args.command == "status":
        t = svc.set_status(args.id, Status[args.status])
        print("Updated" if t else "Not found")
        return 0 if t else 1

    if args.command == "priority":
        t = svc.set_priority(args.id, Priority[args.priority])
        print("Updated" if t else "Not found")
        return 0 if t else 1

    if args.command == "remove":
        ok = svc.remove(args.id)
        print("Removed" if ok else "Not found")
        return 0 if ok else 1

    parser.print_help()
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
