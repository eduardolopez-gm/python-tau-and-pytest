import pytest

@pytest.fixture
def global_values_supplier():
    first_value = 10
    second_value = 20
    third_value = 30
    return [first_value, second_value, third_value]


def test_compare_first_value_with_global_values(global_values_supplier):
    assert global_values_supplier[0] == 10
@pytest.mark.skip
def test_compare_second_value_with_global_values(global_values_supplier):
    assert global_values_supplier[1] == 20

def test_compare_third_value_with_global_values(global_values_supplier):
    assert global_values_supplier[2] == 30
# only add message after assert to show info about the failure otherwise it log basic error
def test_compare_first_value_to_fail(global_values_supplier):
    assert global_values_supplier[0] == 20, 'assertion failed'
@pytest.mark.skip
def test_compare_second_value_to_fail(global_values_supplier):
    assert global_values_supplier[1] == 0
def test_compare_third_value_to_fail(global_values_supplier):
    assert global_values_supplier[2] == 20


