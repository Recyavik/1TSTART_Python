from typing import List, Dict, Tuple
from typing import Optional, Union, Any


first: int = 100
print(first,type(first))

first = 'Первое слово'
print(first,type(first))

second: list = 10.2
print(second, type(second))

second = [1, 2, 3, 4, 5]
print(second, type(second))
"""
имя переменной: тип = значение
""" #

def raznost_numbers(a:int = 0, b:int = 0) -> int:
    return a - b

r = raznost_numbers(5)
print(r)

z: str = 'Аннотация'
list_z: List[str] = list(z)
print(list_z)

def upper_list(lst: List[str]):
    for elem in lst:
        print(elem.upper(), end=' ')

upper_list(list_z)

print(upper_list.__annotations__)

d: Dict[str, int] = {'a': 100, 'b': 200}

arr: List[str | int | float] = ['a', 1, 1.0]

def fun4(value: Union[str, int]) -> Union[float, int]:
    return 10

def fun5(value: str | int) -> float | int:
    return 10

def func3(array: Any) -> Any:
    return 10

lst: Optional[List[str | int | float]] = None

