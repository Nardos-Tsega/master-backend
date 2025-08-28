from pydantic import BaseModel, Field
from typing import Optional, List
from models.unit import UnitInfo

class ConversionRequest(BaseModel):
    value: float = Field(..., gt=-1e100, lt=1e100, description="The value to convert")
    from_unit: str = Field(..., min_length=1, max_length=10, alias="from", description="The unit to convert from")
    to_unit: str = Field(..., min_length=1, max_length=10, alias="to", description="The unit to convert to")
    decimals: Optional[int] = Field(None, ge=0, le=15, description="Number of decimal places to round to")

    class Config:
        allow_population_by_field_name = True

class ConversionResponse(BaseModel):
    value: float
    from_unit: str
    converted_value: float
    to_unit: str
    unit_symbol: str
    conversion_rate: Optional[float] = None
    formatted: Optional[str] = None

    class Config:
        allow_population_by_field_name = True

class CategoryResponse(BaseModel):
    category: str
    units: List[UnitInfo]

class ErrorResponse(BaseModel):
    error: str
    message: str
    detail: Optional[str] = None