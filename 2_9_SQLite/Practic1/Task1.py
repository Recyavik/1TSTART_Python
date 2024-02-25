# https://app.diagrams.net
#   https://www.sqlite.org/
#   https://sqlitestudio.pl/
#   https://sqlitebrowser.org/dl/

import sys

sys.path.append(r"E:\Develop\SQLite")

import sqlite3

conn = sqlite3.connect("n_products_db.db")

# Создание объекта-курсора
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS products (
    id     INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    name   TEXT,
    number INTEGER,
    unit   TEXT DEFAULT ('шт.'),
    price  REAL     DEFAULT (0.0) 
);"""
)
conn.commit()
name_product = "Молоко"
number = 50
price = 100.0

cursor.execute(
    "INSERT INTO products (name, number, price) VALUES (?, ?, ?)",
    (name_product, number, price),
)
cursor.execute("INSERT INTO products (name) VALUES (?)", (name_product,))
conn.commit()
data = [
    ("Хлеб", 40, "бух", 50.5),
    ("Сыр", 30, "кг.", 270.000),
    ("Шоколад", 80, "шт.", 120.25),
]
cursor.executemany(
    "INSERT INTO products (name, number, unit, price) VALUES (?, ?, ?, ?)", data
)
conn.commit()
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT * FROM products")

rows = cursor.fetchall()
# Вывод результатов
for row in rows:
    print(row)

cursor.execute("SELECT * FROM products WHERE number > ?", (100,))

rows = cursor.fetchall()
# Вывод результатов
for row in rows:
    print(row)

cursor.execute("UPDATE products SET price = ? WHERE name = ?", (55.00, "Хлеб"))
conn.commit()
cursor.execute("UPDATE products SET number = ? WHERE number <= ?", (1, 0))

# cursor.execute("DELETE FROM products WHERE name = ?", ('Молоко',))
#
# cursor.execute("DELETE FROM products WHERE price >= ?", (100,))

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()
