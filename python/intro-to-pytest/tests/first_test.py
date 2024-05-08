import pytest
def addition(a,b):
    return a + b

def test_addition():
    assert addition(1, 2) == 3
    assert addition(2, 3) == 5
    

# Example of a test fail 
""" def test_addition_failure():
    assert addition(1, 2) == 4
    assert addition(2, 3) == 6 """
# exception catching
def test_divide_by_Zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert "division by zero" in str(e.value)