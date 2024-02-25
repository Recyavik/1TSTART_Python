# В Python не так уж много инструментов стандартной библиотеки,
# которые работают с шифрованием. Однако, в нашем распоряжении есть библиотека cryptography
# pip install cryptography

import cryptography
from cryptography.fernet import Fernet # для генерации ключей, шифрование и дешифрование
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt # для получения и хранения криптографического ключа
import secrets # для генерации безопасных криптографически надежных чисел и управления секретами
import base64 # для кодирования и декодирования двоичных данных
import getpass # для запроса пароля без его отображения на экране
import argparse # Модуль argparse позволяет разбирать аргументы, передаваемые скрипту
# при его запуске из командной строки, и даёт возможность пользоваться этими аргументами в скрипте

def derive_key(salt, password):
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1) #извлекаем ключ с пароля, используя переданную соль
    return kdf.derive(password.encode())

def load_salt():
    # Криптографическая соль представляет собой данные,
    # которые применяются в процессе хеширования для предотвращения
    # возможности разгадать оригинальный ввод с помощью поиска результата
    # хеширования в списке заранее вычисленных пар ввод-хеш,
    # известном также как "радужная" таблица.
    return open("salt.salt", "rb").read()

def generate_salt(size=16):
    return secrets.token_bytes(size)

def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    if load_existing_salt:
        salt = load_salt()
    elif save_salt:
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)

    derived_key = derive_key(salt, password) # Генерация ключа из соли и пароля
    return base64.urlsafe_b64encode(derived_key) # Вернём сгенерированный ключ с помощью base64



def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

    print("Файл успешно зашифрован")

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Недопустимый токен.")
        return

    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("Файл успешно расшифрован")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скрипт шифрования и дешифрования файла с паролем")
    parser.add_argument("file", help="Файл для шифрования/дешифрования")
    parser.add_argument("-s", "--salt-size",
                        help="Если значение задано, то генерируется новая соль", type=int)
    parser.add_argument("-e", "--encrypt", action="store_true", help="Зашифровать файл")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Расшифровать файл")

    args = parser.parse_args()
    file = args.file

    if args.encrypt:
        password = getpass.getpass("Введите пароль шифрования: ")
    elif args.decrypt:
        password = getpass.getpass("Введите пароль, который вы использовали для шифрования: ")

    if args.salt_size: # Проверяем был ли указан аргумент длины соли
        key = generate_key(password, salt_size=args.salt_size, save_salt=True) #Если да, то генерируем её
    else:
        key = generate_key(password, load_existing_salt=True) #Если нет, то нет

    encrypt_ = args.encrypt # Создадим аргументы о шифровании и дешифровании
    decrypt_ = args.decrypt

    if (encrypt_ and decrypt_):
        raise TypeError("Пожалуйста выбирайте что-то одно: шифровать или дешифровать")
    elif encrypt_:
        encrypt(file, key)
    elif decrypt_:
        decrypt(file, key)
    else:
        TypeError("Пожалуйста выбирайте: шифровать или дешифровать")


# python 3_8_Task2_Hesh.py -s 16 -e test.txt
# python 3_8_Task2_Hesh.py -d test.txt
# python 3_8_Task2_Hesh.py --help