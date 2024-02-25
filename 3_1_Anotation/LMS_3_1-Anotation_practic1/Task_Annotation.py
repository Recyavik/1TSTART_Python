from typing import List
import math


def area_circle(radii_lst: List[int]) -> List[float]:
    answers_list: List[float] = list()
    for radius in radii_lst:
        answers_list.append(round(math.pi * (radius ** 2), 2))
    return answers_list


def circumference(radii_lst: List[int]) -> List[float]:
    answers_list: List[float] = [round(2 * math.pi * radius, 2) for radius in radii_lst]
    return answers_list


r: range = range(20, 100, 10)
lst: List[int] = list(r)
print(lst)

print(area_circle(lst))
print(circumference(lst))
