import pytest
from .solution import is_interesting


@pytest.mark.parametrize(
    "number, awesome_phrases, expected_result",
    [
        (3, [1337, 256], 0),
        (120, [], 1),
        (1232, [], 1),
        (1336, [1337, 256], 1),
        (1337, [1337, 256], 2),
        (1000, [], 2),
        (7890, [], 2),
        (3210, [], 2),
        (11208, [1337, 256], 0),
        (11209, [1337, 256], 1),
        (11211, [1337, 256], 2),
        (987654320, [], 1),
        (987654321, [], 2)
    ]
)
def test_is_interesting(number, awesome_phrases, expected_result):
    assert is_interesting(number, awesome_phrases) == expected_result
