""" think about the different types of testing
for a multiplication
case 1 two positive integers
case 2 two negative integers
case 3 identity: multiply by 1
case 4 zero: multiply by 0
case 5 negative by positive
case 6 floats """

# to avoid repeating, define a tuple list of parameters that 
# will test the function
import pytest


input_params = [
    (2, 3, 6),
    (1, 10, 10),
    (0, 1, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.0, 3.0, 6.0)
]
@pytest.mark.parametrize('a, b, result', input_params)
def test_multiplication(a, b, result):
    assert a * b == result

