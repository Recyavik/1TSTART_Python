# Функция SUM() используется для получения суммы значений в столбце.
# Пример использования:
import sqlite3
# Создание подключения к базе данных
conn = sqlite3.connect('mydatabase.db')
# Создание объекта-курсора
cursor = conn.cursor()
# Выполнение запроса с использованием SUM()
cursor.execute("SELECT SUM(quantity) FROM products")
# Получение результата
result = cursor.fetchone()
# Вывод результата
print("Общее количество продуктов:", result[0])
# Закрытие подключения
conn.close()
