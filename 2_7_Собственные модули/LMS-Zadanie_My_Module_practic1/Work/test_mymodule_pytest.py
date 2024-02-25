# pip install pytest

from MyPackage.myModules import area_trapezoid

def test_area_trapezoid():
    assert area_trapezoid(10, 16, 12) == 156
