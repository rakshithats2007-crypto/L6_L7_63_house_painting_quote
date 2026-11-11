# processor.py

def calculate_paint_gallons(area_sqft):
    """Calculates gallons of paint needed assuming 1 gallon covers 350 sq ft."""
    return round(area_sqft / 350.0, 2)

def parse_room_dimensions(dim_str):
    """Parses room dimensions formatted as 'length,width,height'."""
    parts = dim_str.split(',')
    return {
        "length": float(parts[0]),
        "width": float(parts[1]),
        "height": float(parts[2])
    }

def calculate_total_quote(rate_per_sqft, area_sqft):
    """Calculates total painting quote."""
    return rate_per_sqft * area_sqft

if __name__ == "__main__":
    print("Running initial processor demo...")
    print("Paint for 1400 sq ft:", calculate_paint_gallons(1400))
    print("Room dimensions:", parse_room_dimensions("12.5,10.0,9.0"))
    print("Total quote:", calculate_total_quote(2.5, 1400))