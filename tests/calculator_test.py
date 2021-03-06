"""Testing the Calculator"""

from calculator import Calculator


def tuple_list():
    """Arranging Data for AAA Testing"""
    return 1.0, 2


def test_calculator_add_method():
    """Testing the Calculator Addition"""

    # Act for AAA testing
    result = Calculator.add(tuple_list())

    # Assertion for AAA testing
    assert result == 3


def test_calculator_subtract_method():
    """Testing the Calculator Subtraction"""

    # Act for AAA testing
    result = Calculator.subtract(tuple_list())

    # Assertion for AAA testing
    assert result == -1


def test_calculator_multiply_method():
    """Testing the Calculator Multiplication"""

    # Act for AAA testing
    result = Calculator.multiply(tuple_list())

    # Assertion for AAA testing
    assert result == 2


def test_calculator_divide_method():
    """Testing the Calculator Division"""

    # Act for AAA testing
    result = Calculator.divide(tuple_list())

    # Assertion for AAA testing
    assert result == 0.5


def test_calculator_divide_by_zero():
    """Testing the Calculator Divide by Zero"""
    # Arrange Data for AAA testing
    tuples_list = (3, 0)

    # Act for AAA testing
    result = Calculator.divide(tuples_list)

    # Assertion for AAA testing
    assert result == "Error: Cannot divide by Zero"
