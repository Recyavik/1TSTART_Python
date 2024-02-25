import time
import sys
for minutes in range(0,60): # внешний цикл минут
    for seconds in range(0,60):  # внутренний цикл секунд начинается каждый раз сначала для каждой итерации минуты
        print("\b\b\b\b\b\b\b\b", end="")
        print("{0:2}:{1:2}".format(minutes, seconds), end="")
        time.sleep(1.0)  # пауза между выводом.