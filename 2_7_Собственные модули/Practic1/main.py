from First_package.Sub.sub_module import multi
from First_package.my_first_module import can, learning
try:
    from First_package.Sub.my_castom_module import *
except ImportError:
    print('Не удалось загрузить модуль my_castom_module, используйте альтернативный код')
import sys
sys.path.append(r'E:\Develop')
print(sys.path)

print(multi(10, 20, 30))
can()
learning()
check()

