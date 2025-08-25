# Task Tracker CLI

A simple command-line task management application built with Python that demonstrates the CRUD mindset (Create, Read, Update, Delete) and a clean, layered backend architecture.

This project is intentionally minimal - using only a JSON file for persistence - so you can focus on understanding how data flows through Models → Repository → Service → CLI.

## Project Structure

task_tracker_cli/
│
├── main.py # CLI entry point (argparse)
├── models/
│ └── task.py # Domain models: Task, TaskId, Priority, Status
├── repos/
│ └── json_repo.py # JSON repository (tasks.json)
└── services/
└── task_service.py # Business use-cases wrapping the repo
