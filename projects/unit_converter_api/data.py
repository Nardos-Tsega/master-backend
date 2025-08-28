BASE_UNITS = {
    "length": "m",
    "mass" : "kg",
    "temprature" : "k"
}

UNIT_DATA = {
    # Length units (meter is base)
    "m": {"name": "meter", "category": "length", "factor": 1, "symbol": "m"},
    "km": {"name": "kilometer", "category": "length", "factor": 1000, "symbol": "km"},
    "mi": {"name": "mile", "category": "length", "factor": 1609.344, "symbol": "mi"},
    "ft": {"name": "foot", "category": "length", "factor": 0.3048, "symbol": "ft"},
    "in": {"name": "inch", "category": "length", "factor": 0.0254, "symbol": "in"},
    
    # Mass units (kilogram is base)
    "kg": {"name": "kilogram", "category": "mass", "factor": 1, "symbol": "kg"},
    "g": {"name": "gram", "category": "mass", "factor": 0.001, "symbol": "g"},
    "lb": {"name": "pound", "category": "mass", "factor": 0.453592, "symbol": "lb"},
    "oz": {"name": "ounce", "category": "mass", "factor": 0.0283495, "symbol": "oz"},
    
    # Temperature units (Kelvin is base, requires special handling with offsets)
    "k": {"name": "kelvin", "category": "temperature", "factor": 1, "offset": 0, "symbol": "K"},
    "c": {"name": "celsius", "category": "temperature", "factor": 1, "offset": 273.15, "symbol": "°C"},
    "f": {"name": "fahrenheit", "category": "temperature", "factor": 5/9, "offset": 459.67, "symbol": "°F"},
}

def get_units_by_category():
    categories = {}
    for unit_code, data in UNIT_DATA.items():
        category = data["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append({**data, "unit_code":unit_code})
        
    return categories

UNITS_BY_CATEGORY = get_units_by_category()