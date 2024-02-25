ALPHA = u'абвгдеёжзийклмнопрстуфхцчшщьъэюя'

def encode(from_file_name, to_file_name, step):
    with open(from_file_name, "r", encoding="utf-8") as file_from:
        data = str(file_from.read())
    with open(to_file_name, "w", encoding="utf-8") as file_to:
        new_text = data.translate(str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))
        file_to.write(new_text)
        return new_text

def decode(from_file_name, to_file_name, step):
    with open(from_file_name, "r", encoding="utf-8") as file_from:
        data = str(file_from.read())
    with open(to_file_name, "w", encoding="utf-8") as file_to:
        new_text = data.translate(str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))
        file_to.write(new_text)
        return new_text

print(encode("test.txt", "encode.txt", 2))
print(decode("encode.txt", "new.txt", 2))
print(decode("test2.txt", "new2.txt", 4))

import string

z = string.ascii_letters
print(z)
z_small = string.ascii_uppercase
print(z_small)

digit = string.digits
print(digit)

p = string.punctuation
print(p)

english_alpha = "".join(chr(i) for i in range(65, 90))
print(english_alpha)

russia_alpha = "".join(chr(i) for i in range(1072, 1104))
print(russia_alpha.upper())

import secrets
password = secrets.token_bytes(32)
print(password)

import rsa

(bob_pub, bop_priv) = rsa.newkeys(512)
# print((bob_pub, bop_priv))

message = "Привет Боб".encode("utf-8")
# print(message)

crypto = rsa.encrypt(message, bob_pub)
# print(crypto)

message = rsa.decrypt(crypto, bop_priv)
print(message.decode("utf-8"))

