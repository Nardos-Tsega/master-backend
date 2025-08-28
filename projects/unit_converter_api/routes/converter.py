from fastapi import APIRouter, HTTPException, Query
from data import UNITS_BY_CATEGORY, UNIT_DATA
from models.unit import UnitInfo
from schema.schema import CategoryResponse
from typing import Optional
from exceptions.exceptions import IncompatibleUnitsError, InvalidUnitError
from services.coverter import convert_units as convert, get_conversion_rate
from schema.schema import ConversionResponse

router = APIRouter()

@router.get("/convert")
async def convert_units(
    value:float = Query(..., description="The value to convert"),
    from_unit: str = Query(..., description="Unit to convert from", alias="from"),
    to_unit: str = Query(..., description="Unit to convert to", alias="to"),
    decimals: Optional[int] = Query(None, description="Number of decimal places to round to")
):
    try:
        converted_value = convert(value, from_unit, to_unit, decimals)
        conversion_rate = get_conversion_rate(from_unit, to_unit)
        
        response_data = {
            "value": value,
            "from_unit": from_unit,
            "converted_value": converted_value,
            "to_unit": to_unit,
            "unit_symbol": UNIT_DATA[to_unit]["symbol"],
            "conversion_rate": conversion_rate,
            "formatted": f"{value} {UNIT_DATA[from_unit]['symbol']} is {converted_value} {UNIT_DATA[to_unit]['symbol']}"
        }        
        
        return ConversionResponse(**response_data)
        
    except (InvalidUnitError, IncompatibleUnitsError) as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion error: {str(e)}")

@router.get("/units")
async def list_all_units():
    categories = []
    for category, units in UNITS_BY_CATEGORY.items():
        category_units = [
            UnitInfo(
                unit_code=unit["unit_code"],
                name=unit["name"],
                category=unit["category"],
                symbol=unit["symbol"]
            )
            for unit in units
        ]
        categories.append(CategoryResponse(category=category, units=category_units))
    return categories

@router.get("/units/{category}")
async def list_units_by_category(category: str):
    if category not in UNITS_BY_CATEGORY:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found")
    
    units = [
        UnitInfo(
            unit_code=unit["unit_code"],
            name=unit["name"],
            category=unit["category"],
            symbol=unit["symbol"]
        ) 
        for unit in UNITS_BY_CATEGORY[category]
    ]
    return CategoryResponse(category=category, units=units)