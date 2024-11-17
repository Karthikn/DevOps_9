import pytest
from calculator import divide
def test_divide():
    assert divide(10,1)==10

@pytest.mark.parametrize("a,b, expected", [(5,5,10), (4,6)])

def test_add_parameters(a,b,expected):
    assert add(a,b)==expected