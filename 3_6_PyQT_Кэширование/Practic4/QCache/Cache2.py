from PyQt5.QtCore import QCache

# Создание экземпляра QCache с максимальным количеством элементов
cache = QCache()
cache.setMaxCost(100)  # Установка максимального количества элементов в кэше

# Добавление элементов в кэш
cache.insert("key1", "value1")
cache.insert("key2", "value2")
cache.insert("key3", "value3")

# Получение элемента из кэша
value = cache.object("key1")
print(value)  # Выведет: "value1"

# Проверка наличия элемента в кэше
if cache.contains("key2"):
    print("Key2 is in the cache")

# Удаление элемента из кэша
cache.remove("key3")

# Очистка кэша
cache.clear()
