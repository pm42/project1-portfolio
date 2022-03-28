"""Calculation, Addition, Multiplication, Subtraction and Division Classes """
from calculator.operations import Addition as Add, Subtraction as Sub, Multiplication as Mult, Division as Div
from abc import ABC, abstractmethod


class Calculation:
    """ calculation abstract base class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, tuple_list: tuple):
        """ constructor method"""
        self.__values = Calculation.convert_args_to_tuple_of_float(tuple_list)

    @abstractmethod
    def get_result(self):
        pass

    def get_values(self):
        return self.__values

    @classmethod
    def create(cls, tuple_list: tuple):
        """ factory method"""
        return cls(tuple_list)

    @staticmethod
    def convert_args_to_tuple_of_float(tuple_list):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in tuple_list:
            list_values_float.append(float(item))
        return tuple(list_values_float)


class Addition(Calculation):
    """ calculation addition class"""

    def get_result(self):
        """get the addition results"""
        sum_of_values = 0.0
        for value in self.get_values():
            sum_of_values = Add.add(value, sum_of_values)
        return sum_of_values


class Multiplication(Calculation):
    """multiplication calculation object"""

    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.get_values():
            result = Mult.multiply(result, value)
        return result


class Subtraction(Calculation):
    """subtraction calculation object"""

    def get_result(self):
        """get the subtraction results"""
        difference_of_values = 0.0
        for index, value in enumerate(self.get_values()):
            if index == 0:
                difference_of_values = value
            else:
                difference_of_values = Sub.subtract(difference_of_values, value)
        return difference_of_values


class Division(Calculation):
    """division calculation object"""

    def get_result(self):
        """get the division results"""
        result = 1.0
        for index, value in enumerate(self.get_values()):
            if index == 0:
                result = value
            else:
                result = Div.divide(result, value)
        return result
