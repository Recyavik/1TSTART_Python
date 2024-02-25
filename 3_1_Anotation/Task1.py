# Аннотации позволяют нам код сделать более информативным и связывает нас с динамической типизацией

from typing import Any, Dict
from typing import List, Dict, Tuple
from typing import Optional
from typing import Union

# всё это позволяет код сделать работу с кодом более читаемой для других разработчиков



first = 100
first = 'Анноация'

first:int = 100
print(first, type(first))
first = 'Анноация'
print(first, type(first))

second:int = 200
second = [1, 2, 3, 4, 5]
print(second, type(second))

first:int = 100
second:int = 200
def add_number(a: int, b: int = 11) -> int:
    return a + b

def add_number(a: int, b: Optional[int] = None) -> int:
    return a + b

def add_number(a: int, b: int = 11) -> int:
    return a + b

def upper_list(lst: List[str]):
    for elem in lst:
        print(elem.upper())

print(add_number(first, second))
print(add_number([1, 2, 3], [4, 5, 6]))

# Где хранятся аннотации ?
print(add_number.__annotations__)
# -> int:

print(add_number.__annotations__)


"""

имя переменной: тип = значение
-> int 

Это необязательный инструмент
""" #

d: dict[str, int] = {'a':100, 'b':200}


number = 10
arrange: list[str | int | float]  = ["a", 1, 1.0]
print(arrange)

def funct(number: int, value: list) -> None:
    pass

def funct2(number: int, value: List[str]) -> int:
    return number + len(value)

def funct3(arrage: Any) -> Any:
    return 10

def funct4(value: Union[str, int]) -> Union[str, int]:
    return 10

def funct5(value: str | int) -> str | int:
    return 10




