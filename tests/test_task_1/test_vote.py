from src.task_1.vote import vote
import pytest


@pytest.mark.parametrize('test_input, expected', [([1,1,1,2,3], 1), ([1,2,3,2,2], 2)])
def test_vote(test_input, expected):
    result = vote(test_input)
    assert result == expected, 'Result is not equal to the expected value'
    assert type(result) == type(expected), 'Result and expected value have different types'