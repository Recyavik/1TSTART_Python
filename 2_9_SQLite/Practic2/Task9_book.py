# Рассмотрим пример цельного приложения на Python, использующего SQLite.
# Представим простую книжную библиотеку, в которой пользователи могут добавлять,
# просматривать, обновлять и удалять книги. Вот общая структура такого приложения:

import sqlite3
# Создание подключения к базе данных
conn = sqlite3.connect('library_book.db2')
# Создание объекта-курсора
cursor = conn.cursor()
def create_table():
    # Создание таблицы books
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    year INTEGER
                    )''')
def add_book(title, author, year):
    # Вставка книги в таблицу
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    print("Книга успешно добавлена.")
def view_books():
    # Получение всех книг из таблицы
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute("SELECT COUNT(*) FROM books")
    # Получение результата
    result = cursor.fetchone()
    # Вывод результата
    print("Количество книг:", result[0])
def update_book(id, title, author, year):
    # Обновление книги в таблице
    cursor.execute("UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?", (title, author, year, id))
    conn.commit()
    print("Книга успешно обновлена.")
def delete_book(id):
    # Удаление книги из таблицы
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    print("Книга успешно удалена.")
def main():
    create_table()
    while True:
        print("\n------ Книжная библиотека ------")
        print("1. Добавить книгу")
        print("2. Просмотреть все книги")
        print("3. Обновить книгу")
        print("4. Удалить книгу")
        print("5. Выйти")
        choice = input("Выберите действие (1-5): ")
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            add_book(title, author, year)
        elif choice == '2':
            print("\n--- Список всех книг ---")
            view_books()
        elif choice == '3':
            view_books()
            id = int(input("Введите ID книги, которую хотите обновить: "))
            title = input("Введите новое название книги: ")
            author = input("Введите нового автора книги: ")
            year = int(input("Введите новый год издания книги: "))
            update_book(id, title, author, year)
        elif choice == '4':
            view_books()
            id = int(input("Введите ID книги, которую хотите удалить: "))
            delete_book(id)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
    # Закрытие подключения
    conn.close()
main()

