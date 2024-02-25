import sqlite3
# Создание подключения к базе данных
conn = sqlite3.connect('mydatabase.db')
# Создание объекта-курсора
cursor = conn.cursor()
# Выполнение запроса с использованием MAX()
cursor.execute("SELECT MAX(price) FROM products")
# Получение результата
max_price = cursor.fetchone()[0]
# Выполнение запроса с использованием MIN()
cursor.execute("SELECT MIN(price) FROM products")
# Получение результата
min_price = cursor.fetchone()[0]
# Вывод результатов
print("Максимальная цена:", max_price)
print("Минимальная цена:", min_price)
# Закрытие подключения
conn.close()
