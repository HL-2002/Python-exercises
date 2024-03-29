from fuel_exceptions import convert, fuel_calc


# Fuel convert function
def test_convert_positive():
    # Rational fractions
    assert convert(1 / 2) == 50
    assert convert(3 / 4) == 75
    assert convert(1 / 1) == 100

    # Irrational fractions
    assert convert(49/101) == 49


def test_convert_zero():
    # Zero
    assert convert(0 / 3) == 0


# Fuel gauge calc function
def test_fuel_calc_empty():
    # Empty fuel gauge
    assert fuel_calc(0) == "E"
    assert fuel_calc(1) == "E"


def test_fuel_calc_full():
    # Full fuel gauge
    assert fuel_calc(99) == "F"
    assert fuel_calc(100) == "F"

def test_fuel_calc_other():
    # Other fuel gauge
    assert fuel_calc(50) == "50%"
    assert fuel_calc(49) == "49%"
