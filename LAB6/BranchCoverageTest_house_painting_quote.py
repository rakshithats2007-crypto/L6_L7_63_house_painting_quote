import pytest

from house_painting_quote import crew_days, paint_litres, painting_quote


# ---------------------------------------------------------------------------
# painting_quote() branch coverage
# ---------------------------------------------------------------------------

def test_painting_quote_unknown_paint_raises():
    # Branch: paint not in PAINT_RATE is True
    with pytest.raises(ValueError, match="unknown paint"):
        painting_quote("latex", 200, 1, False)


@pytest.mark.parametrize("area_sqft, coats", [(0, 1), (-10, 1), (100, 0)])
def test_painting_quote_invalid_job_raises(area_sqft, coats):
    # Branch: area_sqft <= 0 or coats < 1 is True
    with pytest.raises(ValueError, match="invalid job"):
        painting_quote("emulsion", area_sqft, coats, False)


def test_painting_quote_distemper_interior_valid():
    # Branch: is_exterior and paint == "distemper" is False
    assert painting_quote("distemper", 600, 1, False) == 7200


def test_painting_quote_exterior_distemper_raises():
    # Branch: is_exterior and paint == "distemper" is True
    with pytest.raises(ValueError, match="distemper is for interiors only"):
        painting_quote("distemper", 300, 2, True)


def test_painting_quote_exterior_surcharge_applied():
    # Branch: is_exterior is True
    assert painting_quote("enamel", 500, 2, True) == 32500


def test_painting_quote_large_area_discount_applied():
    # Branch: area_sqft > 2000 is True
    assert painting_quote("enamel", 2100, 2, False) == 113400


def test_painting_quote_minimum_quote_floor_applied():
    # Branch: cost < 5000 is True
    assert painting_quote("emulsion", 50, 1, False) == 5000


# ---------------------------------------------------------------------------
# paint_litres() branch coverage
# ---------------------------------------------------------------------------

def test_paint_litres_smooth_exact_coverage_no_remainder():
    # Branch: surface == "smooth" is True, needed % coverage == 0
    assert paint_litres(200, 1, "smooth") == 2


def test_paint_litres_smooth_remainder_rounds_up():
    # Branch: surface == "smooth" is True, needed % coverage != 0
    assert paint_litres(250, 1, "smooth") == 3


def test_paint_litres_rough_exact_coverage_no_remainder():
    # Branch: surface == "rough" is True, needed % coverage == 0
    assert paint_litres(120, 1, "rough") == 2


def test_paint_litres_rough_remainder_rounds_up():
    # Branch: surface == "rough" is True, needed % coverage != 0
    assert paint_litres(130, 1, "rough") == 3


def test_paint_litres_unknown_surface_raises():
    # Branch: surface != "smooth" and != "rough" -> else raises ValueError
    with pytest.raises(ValueError, match="unknown surface"):
        paint_litres(100, 1, "textured")


# ---------------------------------------------------------------------------
# crew_days() branch coverage
# ---------------------------------------------------------------------------

def test_crew_days_requires_at_least_one_painter():
    # Branch: painters < 1 is True
    with pytest.raises(ValueError, match="need at least one painter"):
        crew_days(500, 0, False)


def test_crew_days_rounds_up_when_area_has_remainder():
    # Branch: area_sqft % per_day != 0 is True
    assert crew_days(350, 1, False) == 1


def test_crew_days_wallpaper_removal_adds_two_days():
    # Branch: has_wallpaper_removal is True
    assert crew_days(800, 2, True) == 3