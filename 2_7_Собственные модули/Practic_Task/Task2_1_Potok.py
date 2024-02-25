import time
from threading import Thread
import Task2_library2 as potok


potok.first()
potok.second()

th1 = Thread(target=potok.first)
th2 = Thread(target=potok.second)
th1.start()
th2.start()