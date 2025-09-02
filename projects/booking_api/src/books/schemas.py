from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    
class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None