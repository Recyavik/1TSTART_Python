import sqlite3

conn = sqlite3.connect("n_products_db.db")

# Создание объекта курсора
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT,
    number INTEGER,
    unit TEXT DEFAULT ('шт.'),
    price REAL DEFAULT (0.0)
);
""")
conn.commit()

name_product = "Молоко"
number = 50
price = 100.0
cursor.execute(
    """
    INSERT INTO products (name, number, price) VALUES (?, ?, ?)
    """, (name_product, number, price)
)
conn.commit()

name_product = "ХЛЕБ"
number = 15
price = 45
cursor.execute(
    """
    INSERT INTO products (name, number, price) VALUES (?, ?, ?)
    """, (name_product, number, price)
)
conn.commit()

data = [
    ("Сыр", 30, "кг.", 270.00),
    ("Шоколад", 80, "шт.", 120.25),
    ("Яблоко", 40, "кг.", 150.00),
]
cursor.executemany(
    """
    INSERT INTO products (name, number, unit ,price) VALUES (?, ?, ?, ?)  
    """, (data)
)
conn.commit()
cursor.execute(""" SELECT * FROM products WHERE unit = ?""", ('шт.',))
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("""UPDATE products SET price = ? WHERE name = ? """, (55.00, "ХЛЕБ"))
conn.commit()

cursor.execute(""" DELETE FROM products WHERE price > ?""", (100, ))
conn.commit()


conn.close()