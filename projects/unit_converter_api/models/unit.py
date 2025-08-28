from pydantic import BaseModel

class UnitInfo(BaseModel):
    unit_code:str
    name:str
    category:str
    symbol:str