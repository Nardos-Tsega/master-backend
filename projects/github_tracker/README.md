# GitHub Activity Tracker CLI

A simple Python command-line tool that fetches and displays recent **GitHub user activity**.  
It demonstrates clean architecture using **OOP** principles and a layered structure:

- **Client** → Handles GitHub API requests.
- **Parser** → Translates raw GitHub event JSON into human-readable lines.
- **Service** → Orchestrates client and parser.
- **CLI** → Entry point with `argparse`.

---

## 🚀 Features

- Fetches recent public GitHub events for any username.
- Prints activity in a readable format:
