import pytest
from calculator import add,subtract,multiply,divide
def test_add():
    assert add(10,1)==11

def test_subtract():
    assert subtract(16,8)==8

def test_multiply():
    assert multiply(5,5)==25

def test_divide():
    assert divide(10,2)==5

@pytest.mark.parametrize("a,b, expected", [(5,5,10),
                                          (4,5,9),
                                          (3,4,7)      ])

def test_add_parameters(a,b,expected):
    assert add(a,b)==expected




   


