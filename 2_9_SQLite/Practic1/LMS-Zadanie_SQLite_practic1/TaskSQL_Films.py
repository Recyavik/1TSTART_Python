import sqlite3
conn = sqlite3.connect('filmoteka.db')

# Создание объекта-курсора
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS films (
                    id INTEGER PRIMARY KEY,
                    name_film TEXT,
                    genre TEXT,
                    year INTEGER,
                    rating REAL DEFAULT 2.0
                )''')
film_data = [
    ('Мой пёс Руни', 'Мелодрама', 2023, 6.8),
    ('Лохматый патруль', 'Комедия', 2022, 4.5),
    ('Пальма', 'Драма', 2020, 6.9),
    ('Скуби-ду', 'Мультфильм', 2020, 5.6),
    ('Собачья жизнь', 'Семейный', 2019, 7.4),
    ('Того', 'Драма', 2019, 7.9)
]
cursor.executemany("INSERT INTO films (name_film, genre ,year, rating) VALUES (?, ?, ?, ?)", film_data)
print('--------- После вставки списка фильмов ---------')
cursor.execute("SELECT * FROM films")
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.execute("UPDATE films SET rating = ? WHERE year < ?", (6.5, 2020))
print('--------- После обновления рейтинга фильмов до 6.5 старше 2020 года ---------')
cursor.execute("SELECT * FROM films")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("DELETE FROM films WHERE rating < ?", (5,))
print('--------- После удаления фильмов с рейтингом меньше 5 ---------')
cursor.execute("SELECT * FROM films")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()


