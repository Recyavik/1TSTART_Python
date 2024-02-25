# Функция AVG() используется для получения среднего значения столбца.
# Пример использования:

import sqlite3
# Создание подключения к базе данных
conn = sqlite3.connect('mydatabase.db')
# Создание объекта-курсора
cursor = conn.cursor()
# Выполнение запроса с использованием AVG()
cursor.execute("SELECT AVG(price) FROM products")
# Получение результата
result = cursor.fetchone()
# Вывод результата
print("Средняя цена продукта:", result[0])
# Закрытие подключения
conn.close()
