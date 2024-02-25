import sqlite3

conn = sqlite3.connect('library_book.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER  
    )''')

def add_book(title,  author, year):
    cursor.execute(" INSERT INTO books (title, author, year) VALUES (?, ?, ?)", 
    (title,  author, year))
    conn.commit()
    print('Книга успешно добавлена')

def view_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute('SELECT COUNT(*) FROM books')
    result = cursor.fetchone()
    print('Количество книг', result[0])

def update_book(id, title, author, year):
    cursor.execute('UPDATE books SET title =?, author =?, year=? WHERE id= ?',
    ((title, author, year, id))
    conn.commit()
    print('Книга успешно обновлена')

def delete_book(id):
    cursor.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    print('Книга успешно удалена')

def main():
    create_table()
    # Главное пользовательское меню
    while True:
        print("\n ------- Книжная библиотека --------- ")
        print('1. Добавить книгу')
        print('2. Просмотреть все книги')
        print('3. Обновить книгу')
        print('4. Удалить книгу')
        print('5. Выход из программы')
        choice = input('Выберите действие (1-5): ')
        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            year = input('Введите год издания  книги: ')
            add_book(title, author, year)
        elif choice == '2':
            print('\n **** Список всех книг ***** ')
            view_books()
        elif choice == '3':
            view_books()
            id = int(input('Введите ID книги, которую хотите обновить: '))
            title = input('Введите новое название книги: ')
            author = input('Введите нового автора книги: ')
            year = input('Введите новый год издания  книги: ')
            update_book(id, title, author, year)
        elif choice == '4':
            view_books()
            id = int(input('Введите ID книги, которую хотите удалить: '))
            delete_book(id)
        elif choice == '5':
            break
        else:
            print('Неверный выбор. Попробуйте снова')

    conn.close()


if __name__ == '__main__':
    main()

# https://blog.eldorado.ru/publications/luchshie-knigi-po-itogam-2023-goda-pishcha-dlya-dushi-i-uma-40131