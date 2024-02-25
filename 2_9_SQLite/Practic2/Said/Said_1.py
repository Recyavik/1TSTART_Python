import sqlite3

conn = sqlite3.connect('new_db.db')

cursor = conn.cursor()
# cursor.execute('''
# DROP TABLE IF EXISTS products; # Удаление таблицы
# ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    id     INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    name   TEXT,
    number INTEGER  DEFAULT 0,
    unit_id   REFERENCES units,
    price  REAL (12, 2) DEFAULT (0.00)
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS units (
    id     INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    name   TEXT(4) DEFAULT ('шт.')
);''')
try:
    cursor.execute('''INSERT INTO units  VALUES (1, 'шт.');''')
except sqlite3.IntegrityError:
    print('Запись уже существует')
cursor.execute('''INSERT INTO units (name) VALUES ('гр.');''')

data = [('л.',), ('кг.',), ('уп.',)]
# executemany
cursor.executemany('''INSERT INTO units (name) VALUES (?);''', data)

cursor.execute('''SELECT * FROM products''')
print("---------------------------------------")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''SELECT name, price FROM products''')
print("---------------------------------------")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''SELECT name FROM units''')
print("---------------------------------------")
rows = cursor.fetchall()
for row in rows:
    print(row[0])

cursor.execute('''UPDATE units SET name = 'грамм.' WHERE name = 'гр.';''')

cursor.execute('''DELETE FROM units WHERE name = 'уп.';''')


conn.commit()
cursor.close()
