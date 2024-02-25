from module_example import *

def test_add():
    assert add(3, 5) == 8
    assert add(-3, 5) == 2
    assert add(0, 0) == 0

def test_multi():
    assert multi(3, 5) == 15
    assert multi(-3, 5) == -15

# pip install pytest