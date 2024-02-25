### Подключение модуля к программе на Python осуществляется с помощью оператора import.
### У него есть две формы: import и from-import:
### В первом случае пространство имен модуля остается в отдельном имени, и для доступа
### к конкретному имени из модуля нужно применять точку.
from Task1_1_library import i_can, i_learning, multiply as lb
i_learning()
i_can()

result = multiply(10, 20)
print(result)

# import library as lb
# lb.i_learning()
# lb.i_can()

### Во втором случае имена используются так, как если бы
### они были определены в текущем модуле:

# from library import *
# i_learning()
# i_can()

### С помощью первой формы с текущей областью видимости связывается только имя,
### ссылающееся на объект модуля, а при использовании второй — указанные имена
### (или все имена, если применен символ *) объектов модуля связываются с текущей областью видимости.

# from library import i_can, i_learning
# i_learning()
# i_can()



