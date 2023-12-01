from app.calculator import Calculator

def test_addition_positive():
    calc = Calculator(3, 4)
    result = calc.addition()
    assert result == 7

def test_addition_negative():
    calc = Calculator(-3, 4)
    result = calc.addition()
    assert result == 1

def test_addition_float():
    calc = Calculator(2.5, 3.5)
    result = calc.addition()
    assert result == 6.0

def test_subtraction_positive():
    calc = Calculator(5, 2)
    result = calc.subtraction()
    assert result == 3

def test_subtraction_negative():
    calc = Calculator(2, 5)
    result = calc.subtraction()
    assert result == -3

def test_subtraction_float():
    calc = Calculator(8.5, 3.5)
    result = calc.subtraction()
    assert result == 5.0
