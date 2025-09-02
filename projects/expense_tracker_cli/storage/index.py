from typing import Dict, Any

class Storage:
    def load(self) -> Dict[str, Any]:
        raise NotImplementedError
    
    def save(self, data: Dict[str,Any]) -> None:
        raise NotImplementedError