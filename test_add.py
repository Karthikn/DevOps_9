import pytest
from calculator import add
def test_add():
    assert add(10,1)==11
    assert add(10,5)==15