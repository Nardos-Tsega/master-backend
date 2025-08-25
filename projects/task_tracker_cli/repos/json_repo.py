from pathlib import Path
import json
from models.task import Task, TaskId
from typing import Optional, List

class JsonTaskRepo:
    def __init__(self, file_path: str = "tasks.json"):
        self.path = Path(file_path)
        if not self.path.exists():
            self._atomic_write({"tasks": []})
    
    # ----------- Public API -----------
    def add(self, task:Task) -> None:
        data = self._read_all()
        data["tasks"].append(task.to_dict())
        self._atomic_write(data)
    
    def get(self, task_id:TaskId) -> Optional[Task]:
        data = self._read_all()    
        for t in data["tasks"]:
            if t["id"] == task_id.value:
                return Task.from_dict(t)
        
        return None
        
    def list(self) -> List[Task]:
        data = self._read_all()
        return [Task.from_dict(t) for t in data["tasks"]]
    
    def update(self, task: Task) -> bool:
        data = self._read_all()
        tasks = data["tasks"]
        for i, t in enumerate(tasks):
            if t["id"] == task.id.value:
                tasks[i] = task.to_dict()
                self._atomic_write(data)
                return True
        return False
    
    def remove(self, task_id:TaskId) -> bool:
        data = self._read_all()
        before = len(data["tasks"])
        data["tasks"] = [t for t in data["tasks"] if t["id"] != task_id.value]
        if len(data["tasks"]) != before:
            self._atomic_write(data)
            return True
        return False
    
    def _read_all(self):
        try:
            with self.path.open("r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    return data
                except json.JSONDecodeError:
                    return {"tasks": []}
        except FileNotFoundError:
            data = {"tasks":[]}
            
        if "tasks" not in data or not isinstance(data["tasks"], list):
            data = {"tasks": []}
        return data
    
    def _atomic_write(self, data):
        tmp = self.path.with_suffix(".tmp")
        with tmp.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
            
        tmp.replace(self.path)