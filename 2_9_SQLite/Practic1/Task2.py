import sqlite3
# Создание подключения к базе данных
conn = sqlite3.connect('products_db.db')
# Если база данных не существует, она будет создана автоматически.

# Создание объекта-курсора
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    number INTEGER DEFAULT 0,
                    price REAL DEFAULT 0.0
                )''')
try:
    # Создание индекса на столбце 'name' в таблице 'users'
    cursor.execute("CREATE INDEX idx_name ON users (name)")
except (sqlite3.OperationalError):
    print('Нельзя создать индексы повторно!')

data = [
    ('Хлеб', 40, 50.5),
    ('Сыр', 30, 270.000),
    ('Шоколад', 80, 120.25)
]
cursor.executemany("INSERT INTO products (name, number, price) VALUES (?, ?, ?)", data)

cursor.execute("PRAGMA optimize")
cursor.execute("SELECT * FROM products WHERE number > ?", (1,))
# Получение результатов
rows = cursor.fetchall()
# Вывод результатов
for row in rows:
    print(row)

try:
    # Начало транзакции
    conn.execute("BEGIN")
    # Выполнение операций в рамках транзакции
    cursor.execute("INSERT INTO products (name, number, price) VALUES (?, ?, ?)", ('Торт', 5, 400.0))
    cursor.execute("UPDATE products SET price = ? WHERE name = ?", (30, 'Хлеб'))
    # Завершение транзакции
    conn.commit()
except Exception as e:
    # Откат транзакции в случае ошибки
    conn.rollback()
    print("Ошибка:", str(e))

# Выполнение вложенного запроса
cursor.execute("SELECT name FROM products WHERE price > (SELECT AVG(price) FROM products)")
# Получение результатов
rows = cursor.fetchall()
# Вывод результатов
for row in rows:
    print(row[0])

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()
