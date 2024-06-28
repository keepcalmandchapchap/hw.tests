from src.task_1.quadratic_equation import solution
import pytest


@pytest.mark.parametrize('test_input, expected', [((1, 8, 15), '-3.0 -5.0'),((1, -13, 12), '12.0 1.0'),((-4, 28, -49), '3.5'), ((1, 1, 1), 'корней нет')])
def test_quadratic_equation(test_input, expected):
    result = solution(test_input)
    assert result == expected, 'Result is not equal to the expected value'
    assert type(result) == type(expected), 'Result and expected value have different types'


