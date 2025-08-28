from data import UNIT_DATA, BASE_UNITS
from exceptions.exceptions import InvalidUnitError, IncompatibleUnitsError

def convert_units(value:float, from_unit:str, to_unit:str, decimals:int = None) -> float:
    if from_unit not in UNIT_DATA:
        raise InvalidUnitError(from_unit)
    if to_unit not in UNIT_DATA:
        raise InvalidUnitError(to_unit)
    
    from_data = UNIT_DATA[from_unit]
    to_data = UNIT_DATA[to_unit]
    
    if from_data["category"] != to_data["category"]:
        raise IncompatibleUnitsError(from_data["category"], to_data["category"])
    
    category = from_data["category"]
    base_unit = BASE_UNITS[category]
    
    if category == "temprature":
        value_in_base = (value - from_data.get("offset", 0)) / from_data.get("factor", 1)
        result = value_in_base * to_data.get("factor", 1) + to_data.get("offset", 0)
    else:
        value_in_base = value * from_data["factor"]
        result = value_in_base / to_data["factor"]
        
    if decimals is not None:
        result = round(result, decimals)
        
    return result

def get_conversion_rate(from_unit:str, to_unit:str) -> float:
    if UNIT_DATA[from_unit]["category"] == "temperature":
        return None
        
    return convert_units(1, from_unit, to_unit)