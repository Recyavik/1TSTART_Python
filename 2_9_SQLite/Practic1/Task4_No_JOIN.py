import sqlite3
# Создание подключения к базе данных
conn = sqlite3.connect('products_db.db')
# Создание объекта-курсора
cursor = conn.cursor()
# Выполнение объединения (JOIN)
cursor.execute("SELECT users.name, orders.order_date FROM users JOIN orders ON users.id = orders.user_id")
# Получение результатов
rows = cursor.fetchall()
# Вывод результатов
for row in rows:
    print(row[0], row[1])
# Закрытие подключения
conn.close()
