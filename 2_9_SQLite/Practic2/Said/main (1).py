import sqlite3


con = sqlite3.connect('db/second.db')
cursor = con.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author_id INTEGER,
    year INTEGER,
    circulation INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);''')


books_query = """
INSERT INTO books(title, author_id, year, circulation)
VALUES(?, ?, ?, ?);
"""
books_data = [
    ('Война и мир', 1, 1880, 5000000),
    ('Анна Каренина', 1, 1877, 30000000),
    ('Колобок', None, 1500, 6000000),
    ('Бойцовский клуб', 2, 1988, 2000000)
]
# cursor.executemany(books_query, books_data)


authors_query = """
INSERT INTO authors(name)
VALUES(?);
"""
authors_data = [
    ('Лев Толстой',),
    ('Чак Паланик',),
    ('Пушкин А.С.',)
]
# cursor.executemany(authors_query, authors_data)

# Агрегирующие функции
# COUNT, SUM, AVG, MIN, MAX

result = cursor.execute("""
SELECT author_id, COUNT()
FROM books
GROUP by author_id;
""").fetchall()

result = cursor.execute("""
SELECT author_id, SUM(circulation)
FROM books
GROUP by author_id
HAVING SUM(circulation) > 10000000;
""").fetchall()


# JOIN

# Плохой способ
# result = cursor.execute("""
# SELECT *
# FROM books, authors
# WHERE books.author_id = authors.id;
# """).fetchall()


# result = cursor.execute("""
# SELECT *
# FROM books
# INNER JOIN authors ON books.author_id = authors.id
# """).fetchall()
# print(result)

# result = cursor.execute("""
# SELECT *
# FROM books
# LEFT JOIN authors ON books.author_id = authors.id
# """).fetchall()
# print(result)

# result = cursor.execute("""
# SELECT *
# FROM books
# RIGHT JOIN authors ON books.author_id = authors.id
# """).fetchall()
# print(result)


result = cursor.execute("""
SELECT books.title, authors.name, books.year, books.circulation
FROM books
LEFT JOIN authors ON books.author_id = authors.id
""").fetchall()
print(result)

con.commit()
con.close()
