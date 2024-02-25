from PyQt6.QtCore import QCache

# Создание экземпляра QCache с максимальным количеством элементов 100
cache = QCache()
cache.setMaxCost(100)

# Добавление элемента в кэш
cache.insert("key1", "value1")

# Получение элемента из кэша
value = cache.object("key1")
if value is not None:
    print(value)

# Удаление элемента из кэша
cache.remove("key1")

# Проверка наличия элемента в кэше
if cache.contains("key1"):
    print("Элемент key1 находится в кэше")
else:
    print("Элемент key1 отсутствует в кэше")

# Очистка кэша
cache.clear()
