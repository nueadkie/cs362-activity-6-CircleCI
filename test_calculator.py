"""
Unit tests using pytest for calculator
"""


import calculator


class TestCalculator:

    def test_add(self):
        assert 6 == calculator.add(1, 5)

    def test_subtract(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self):
        assert 12 == calculator.multiply(3, 4)

    def test_divide(self):
        assert 5 == calculator.divide(25, 5)
