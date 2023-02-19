def optional_comma_float(data):
    """Utility function to convert invalid comma separated floats"""
    return float(data.replace(",", ".")) if data else None
