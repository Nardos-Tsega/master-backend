from storage.index import Storage
from typing import Dict, Any
from pathlib import Path
import json

class JSONStorage(Storage):
    def __init__(self, filepath:Path):
        self.filepath = filepath
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        
    def load(self) -> Dict[str, Any]:
        if not self.filepath.exists():
            return {"expenses": []}
        
        with self.filepath.open("r", encoding="utf-8") as f:
            text = f.read().strip()
            if not text:
                return {"expenses": []}
        
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            return {"expenses": []}

        if not isinstance(data, dict) or "expenses" not in data or not isinstance(data["expenses"], list):
            return {"expenses": []}

        return data
    
    def save(self, data:Dict[str, Any]) -> None:
        with self.filepath.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)