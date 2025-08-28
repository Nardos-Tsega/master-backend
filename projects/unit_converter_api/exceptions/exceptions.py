from fastapi import HTTPException, status

class InvalidUnitError(HTTPException):
    def __init__(self, unit_code:str):
        detail = f"Unit {unit_code} is not recognized. Use /units endpoint to see available units"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
        
class IncompatibleUnitsError(HTTPException):
    def __init__(self, category1:str, category2:str):
        detail = f"Cannot convert between '{category1}' and '{category2}'. Units must be of the same category"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)