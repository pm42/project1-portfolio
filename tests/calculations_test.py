"""Testing the Calculator"""

from calculator.calculations import Addition, Subtraction, Multiplication, Division


def test_calculation_multiplication_instance():
    """Testing the Calculator Multiplication"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert isinstance(calculation, Multiplication)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtraction"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert isinstance(calculation, Subtraction)


def test_calculation_addition_instance():
    """Testing the Calculator Addition"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert isinstance(calculation, Addition)


def test_calculation_division_instance():
    """Testing the Calculator Addition"""
    tuple_list = (1, 2)
    calculation = Division.create(tuple_list)
    assert isinstance(calculation, Division)


def test_calculation_add_get_result_method():
    """Testing the Calculator Addition Results"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert calculation.get_result() == 3


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtraction Results"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert calculation.get_result() == -1


def test_calculation_multiply_get_result_method():
    """Testing the Calculator Multiplication Results"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert calculation.get_result() == 2

def test_calculation_divide_get_result_method():
    """Testing the Calculator Division Results"""
    tuple_list = (1, 2)
    calculation = Division.create(tuple_list)
    assert calculation.get_result() == 0.5
