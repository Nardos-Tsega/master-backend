from repos.json_repo import JsonTaskRepo
from models.task import TaskId, Priority, Status, Task

class TaskService:
    def __init__(self, repo: JsonTaskRepo):
        self.repo = repo
        
    def add(self, title:str,*, priority: Priority = Priority.MEDIUM):
        task = Task(id=TaskId.new(), title=title.strip(),priority=priority)
        self.repo.add(task)
        return task
    
    def get(self, task_id:str):
        return self.repo.get(TaskId(task_id))
    
    def list(self):
        return self.repo.list()
    
    def set_status(self, task_id: str, status: Status):
        task = self.repo.get(TaskId(task_id))
        if not task:
            return None
        
        task.status = status
        self.repo.update(task)
        return task
    
    def set_priority(self, task_id: str, priority: Priority):
        task = self.repo.get(TaskId(task_id))
        if not task:
            return None
        
        task.priority = priority
        self.repo.update(task)
        return task
    
    def remove(self, task_id:str):
        return self.repo.remove(TaskId(task_id))