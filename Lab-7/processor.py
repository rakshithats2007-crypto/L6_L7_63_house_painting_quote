# processor.py

def clean_colour_name(name):
    """
    Turns a colour name into a lower-case code, e.g. 'Ocean Blue' -> 'ocean_blue'.
    Hardened against None and non-string inputs.
    """
    if not isinstance(name, str):
        return ""
    return name.strip().lower().replace(' ', '_')

def room_area(text):
    """
    Converts 'LENGTHxWIDTH' into an area in square feet.
    Hardened against None, missing 'x', and non-numeric values.
    """
    if not isinstance(text, str) or 'x' not in text.lower():
        return 0
    try:
        parts = text.lower().split('x')
        if len(parts) != 2:
            return 0
        return int(parts[0]) * int(parts[1])
    except ValueError:
        return 0

def total_wall_area(text):
    """
    Adds up wall areas separated by semicolons.
    Hardened against None and invalid integer values.
    """
    if not isinstance(text, str):
        return 0
    total = 0
    for area in text.split(';'):
        try:
            cleaned_area = area.strip()
            if cleaned_area:
                total += int(cleaned_area)
        except ValueError:
            pass
    return total

def main():
    print("==== Running clean_colour_name ====")
    try:
        value = input("Enter a paint colour name (e.g. Ocean Blue): ")
        print("Colour code:", clean_colour_name(value))
    except Exception as e:
        print("Error:", e)

    print("\n==== Running room_area ====")
    try:
        value = input("Enter room size as LENGTHxWIDTH in feet (e.g. 12x10): ")
        print("Room area (sq ft):", room_area(value))
    except Exception as e:
        print("Error:", e)

    print("\n==== Running total_wall_area ====")
    try:
        value = input("Enter wall areas separated by ; (e.g. 120;95;110): ")
        print("Total wall area (sq ft):", total_wall_area(value))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()