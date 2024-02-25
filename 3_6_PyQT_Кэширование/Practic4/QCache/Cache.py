# py -m pip --version
# py -m pip install --upgrade pip setuptools wheel
# py -m pip install --user virtualenv
# py -m pip install qcache
# py -m pip install qcache==0.9.3

from PyQt5.QtCore import QCache

# Создаем экземпляр QCache с максимальным количеством элементов
cache = QCache()

# Добавляем элемент в кэш
key = "my_key"
value = "my_value"
cache.insert(key, value)

# Получаем элемент из кэша по ключу
cached_value = cache.object(key)
if cached_value is not None:
    print("Значение из кэша:", cached_value)

# Проверяем наличие элемента в кэше
if cache.contains(key):
    print("Элемент с ключом", key, "находится в кэше")

# Удаляем элемент из кэша
cache.remove(key)

# Очищаем кэш
cache.clear()
