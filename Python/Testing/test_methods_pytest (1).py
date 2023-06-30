from methods_pytest import add, div
from unittest import TestCase
import pytest

class TestAdd2:
    @pytest.mark.parametrize(
            ('val1', 'val2', 'ans'),
            (
                (2, 7, 9),
                (2, -2, 0),
                (2, 0, ValueError)
            )
    )
    
    def test_add(self, val1, val2, ans):
        assert add(val1, val2) == ans, 'This is wrong silly!'

class TestDiv:
    @pytest.mark.parametrize(
        ('num1', 'num2', 'result'), 
        (
            (9, 3, 3),
            (15, 3, 5)
        )

    )
    

    def test_div(self, num1, num2, result):
        assert div(num1, num2) == result

    """def test_add2(self):
        print('test 2')
        assert add(2, -2) == 0

    def test_add4(self):
        assert add(2, 0) == ValueError, 'Val 2 cannot be a zero.'"""

class TestAdd(TestCase):
    def test_add3(self):
        self.assertEqual(add(-4, -3), -7)

    