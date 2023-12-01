import pytest

from app.calculator import Calculator

''' Позитивні тести '''
def test_positive_addition():
    calc = Calculator(3, 4)
    result = calc.addition()
    assert result == 7

def test_positive_subtraction():
    calc = Calculator(5, 2)
    result = calc.subtraction()
    assert result == 3

def test_positive_multiplication():
    calc = Calculator(2, 3)
    result = calc.multiplication()
    assert result == 6

def test_positive_multiplication_float():
    calc = Calculator(2.5, 2)
    result = calc.multiplication()
    assert result == 5.0

def test_positive_division():
    calc = Calculator(8, 4)
    result = calc.division()
    assert result == 2

def test_positive_exponentiation():
    calc = Calculator(2, 3)
    result = calc.exponentiation()
    assert result == 8

''' Негативні тести '''
def test_negative_addition():
    calc = Calculator(-3, 4)
    result = calc.addition()
    assert result == 1

def test_negative_subtraction():
    calc = Calculator(2, 5)
    result = calc.subtraction()
    assert result == -3

def test_negative_multiplication():
    calc = Calculator(-2, 3)
    result = calc.multiplication()
    assert result == -6

def test_negative_multiplication_float():
    calc = Calculator(4.5, -3)
    result = calc.multiplication()
    assert result == -13.5
def test_negative_division():
    calc = Calculator(8, 0)
    result = calc.division()
    assert result == "Error: Division by zero"

def test_negative_exponentiation():
    calc = Calculator(-2, 3)
    result = calc.exponentiation()
    assert result == -8


