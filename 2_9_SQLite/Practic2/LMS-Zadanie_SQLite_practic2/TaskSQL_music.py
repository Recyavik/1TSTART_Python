# Рассмотрим пример цельного приложения на Python, использующего SQLite.
# Представим простую фонотеку, в которой пользователи могут добавлять,
# просматривать, обновлять и удалять треки. Вот общая структура такого приложения:
import sqlite3
# Создание подключения к базе данных
conn = sqlite3.connect('karaoke.db')
# Создание объекта-курсора
cursor = conn.cursor()
def create_table():
    # Создание таблицy треков
    cursor.execute('''CREATE TABLE IF NOT EXISTS music (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    language TEXT,
                    time REAL
                    )''')
def add_music(title, language, time):
    # Вставка трека в таблицу
    time = float(time)
    cursor.execute("INSERT INTO music (title, language, time) VALUES (?, ?, ?)", (title, language, time))
    conn.commit()
    print("Трек успешно добавлен")
def view_music_library():
    # Получение всех треков из таблицы
    cursor.execute("SELECT * FROM music")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def update_music(id, title, language, time):
    # Обновление трека в таблице
    time = float(time)
    cursor.execute("UPDATE music SET title = ?, language = ?, time = ? WHERE id = ?",
                   (title, language, time, id))
    conn.commit()
    print("Название трека успешно обновлено")
def delete_music(id):
    # Удаление трека из таблицы
    cursor.execute("DELETE FROM music WHERE id = ?", (id,))
    conn.commit()
    print("Название песни из каталога удалено")
def main():
    create_table()
    while True:
        print("\n------ Караоке ------")
        print("1. Добавить трек")
        print("2. Просмотреть все треки")
        print("3. Обновить трек")
        print("4. Удалить трек")
        print("5. Выйти")
        choice = input("Выберите действие (1-5): ")
        if choice == '1':
            title = input("Введите название трека: ")
            language = input("Введите язык караоке текста: ")
            time = float(input("Введите время трека: "))
            add_music(title, language, time)
        elif choice == '2':
            print("\n--- Список всех треков ---")
            view_music_library()
        elif choice == '3':
            view_music_library()
            id = int(input("Введите ID песни, которую хотите обновить: "))
            title = input("Введите новое название песни: ")
            language = input("Введите язык караоке текста: ")
            time = float(input("Введите продолжительность этого трека: "))
            update_music(id, title, language, time)
        elif choice == '4':
            id = int(input("Введите ID песни, которую хотите удалить: "))
            delete_music(id)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
        # Закрытие подключения
    conn.close()
main()
