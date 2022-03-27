""" This is the Calculator Class"""
from calculator.calculations import Addition, Subtraction, Multiplication, Division


class Calculator:

    @staticmethod
    def add(tuple_list):
        """ This is the add method"""
        calculation = Addition.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def subtract(tuple_list):
        """ This is the subtract method"""
        calculation = Subtraction.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def multiply(tuple_list):
        """ This is the multiplication method"""
        calculation = Multiplication.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def divide(tuple_list):
        """ This is the division method"""
        calculation = Divison.create(tuple_list)
        return calculation.get_result()