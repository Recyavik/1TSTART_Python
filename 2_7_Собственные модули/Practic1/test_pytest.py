from module_example import *

def test_add():
    assert add(3, 5) == 8
    assert add(-3, 5) == 2

def test_multi():
    assert multi(3, 5) == 15
    assert multi(-3, 5) == -15

