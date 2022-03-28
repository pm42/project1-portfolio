"""Testing the calculator operations """

from calculator.operations import Addition, Subtraction, Multiplication, Division


def test_calculator_operations_add():
    """Testing the Calculator addition"""
    assert Addition.add(2, 3) == 5


def test_calculator_operations_subtract():
    """Testing the Calculator subtraction"""
    assert Subtraction.subtract(1, 3) == -2


def test_calculator_operations_multiply():
    """Testing the Calculator multiplication"""
    assert Multiplication.multiply(3, 2) == 6


def test_calculator_operations_divide():
    """Testing the Calculator division"""
    assert Division.divide(3, 2) == 1.5


def test_calculator_operations_divide_by_zero():
    """Testing the Calculator division by zero"""
    assert Division.divide(3, 0) == "Error: Cannot divide by Zero"
