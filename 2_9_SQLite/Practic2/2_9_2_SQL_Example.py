import sqlite3

conn = sqlite3.connect("SQL_library_books.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS books 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER)
""")
    conn.commit()

def add_book(title, author, year):
    cursor.execute("""
    INSERT INTO books (title, author, year) VALUES (?, ?, ?) """,
    (title, author, year))
    conn.commit()
    print("Книга успешно добавлена")

def view_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute("""SELECT COUNT(*) FROM books""")
    result = cursor.fetchone()
    print("Количество книг", result[0])

def update_book(id, title, author, year):
    cursor.execute("""UPDATE books SET title=?, author=?, year=? WHERE id = ?""",
                   (title, author, year, id))
    conn.commit()
    print("Книга обновлена успешно!")

def delete_book(id):
    cursor.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    print("Книга удалена!")

def main():
    create_table()
    while True:
        print("\n -------- Книжная библиотека ----------")
        print("1. Добавить книгу")
        print("2. Показать книги")
        print("3. Редактировать запись в БД")
        print("4. Удалить книгу")
        print("5. Выход")
        choice = input("Выберите действие (1-5):")
        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            add_book(title, author, year)
        elif choice == "2":
            print("\n **** Список всех книг ****")
            view_books()
        elif choice == "3":
            view_books()
            id = int(input("Введите id книги, которую хотите редактировать:"))
            title = input("Введите новое название книги: ")
            author = input("Введите нового автора книги: ")
            year = input("Введите новый год издания книги: ")
            update_book(id, title, author, year)
        elif choice == "4":
            view_books()
            id = int(input("Введите id книги, которую хотите удалить:"))
            delete_book(id)
        elif choice == "5":
            break
        else:
            print("Не верный выбор, попробуйте снова!")
    conn.close()

if __name__ == "__main__":
    main()
