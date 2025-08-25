Task Tracker CLI
A simple command-line task management application built with Python that demonstrates the CRUD mindset (Create, Read, Update, Delete) and a clean, layered backend architecture.

This project is intentionally minimal - using only a JSON file for persistence - so you can focus on understanding how data flows through Models → Repository → Service → CLI.

🏗️ Project Structure
text
task_tracker_cli/
│
├── main.py # CLI entry point (argparse)
├── models/
│ └── task.py # Domain models: Task, TaskId, Priority, Status
├── repos/
│ └── json_repo.py # JSON repository (tasks.json)
└── services/
└── task_service.py # Business use-cases wrapping the repo
🔗 How the Pieces Connect
text
flowchart TD
A[CLI (main.py)] --> B[TaskService (services/task_service.py)]
B --> C[JsonTaskRepo (repos/json_repo.py)]
C --> D[(tasks.json)]
CLI: Parses commands and prints results

Service: Creates IDs, trims titles, updates status/priority

Repository: Saves/loads Task objects to/from tasks.json

🚀 Setup
bash
git clone <repo-url>
cd task_tracker_cli
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

# No external dependencies needed; standard library only

python main.py --help
🧩 Domain Model
TaskId.new() generates a unique ID (UUID)

Task is a dataclass with to_dict()/from_dict() for JSON serialization

Priority & Status are enums to prevent invalid values

Example usage (inside the code):

python
task = Task(id=TaskId.new(), title="Buy milk", priority=Priority.HIGH)

# Default status: Status.IN_PROGRESS

🛠️ Commands
Command Description
python main.py add "TITLE" [--priority LOW|MEDIUM|HIGH] Add a new task
python main.py list List all tasks
python main.py get <TASK_ID> Show details for a specific task
python main.py status <TASK_ID> <STATUS> Set task status (IN_PROGRESS/DONE/CANCELLED)
python main.py priority <TASK_ID> <PRIORITY> Set task priority (LOW/MEDIUM/HIGH)
python main.py remove <TASK_ID> Delete a task
📖 Example Walkthrough
Add a task

bash
python main.py add "Buy milk" --priority HIGH

# → Added: 6c88c3c0-... (HIGH)

List tasks

bash
python main.py list

# • 6c88c3c0-... | Buy milk | HIGH | IN_PROGRESS | 2025-08-25 12:00:00

Update status

bash
python main.py status 6c88c3c0-... DONE

# → Updated

Get details

bash
python main.py get 6c88c3c0-...

# ✓ 6c88c3c0-... | Buy milk | HIGH | DONE | 2025-08-25 12:00:00

Remove task

bash
python main.py remove 6c88c3c0-...

# → Removed

🤔 Why This Structure?
Separation of concerns:

Model = shape of data

Repository = persistence details (JSON today, DB tomorrow)

Service = business rules / use-cases

CLI = user interface (just parsing & printing)

Testability: Services can be tested with a fake repo; no file I/O in unit tests

Extensibility: Add features (search, due dates, tags) in the service without touching the CLI or storage format

🧠 Learning Outcomes
CRUD fundamentals in a small, real project

Designing simple, maintainable backends

Python tools: dataclasses, Enum, argparse, file I/O, JSON

Simply copy and paste this content into your README.md file. The formatting uses standard Markdown syntax that will render properly on GitHub and other platforms.
