import sqlite3
# Создание подключения к базе данных
conn = sqlite3.connect('library_book.db')
# Создание объекта-курсора
cursor = conn.cursor()
# Функция COUNT() используется для подсчета числа строк, удовлетворяющих заданному условию.
# Выполнение запроса с использованием COUNT()
cursor.execute("SELECT COUNT(*) FROM books")
# Получение результата
result = cursor.fetchone()
# Вывод результата
print("Количество книг:", result[0])
# Закрытие подключения
conn.close()
