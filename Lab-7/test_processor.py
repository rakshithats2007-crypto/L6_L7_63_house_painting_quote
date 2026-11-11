# test_processor.py
from hypothesis import given, strategies as st
from processor import calculate_paint_gallons, parse_room_dimensions, calculate_total_quote

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_calculate_paint_gallons_fuzz(area):
    try:
        calculate_paint_gallons(area)
    except Exception as e:
        assert False, f"calculate_paint_gallons crashed with: {type(e).__name__}: {e}"

@given(st.text())
def test_parse_room_dimensions_fuzz(dim_str):
    try:
        parse_room_dimensions(dim_str)
    except Exception as e:
        assert False, f"parse_room_dimensions crashed with: {type(e).__name__}: {e}"

@given(st.floats(allow_nan=False, allow_infinity=False), st.floats(allow_nan=False, allow_infinity=False))
def test_calculate_total_quote_fuzz(rate, area):
    try:
        calculate_total_quote(rate, area)
    except Exception as e:
        assert False, f"calculate_total_quote crashed with: {type(e).__name__}: {e}"