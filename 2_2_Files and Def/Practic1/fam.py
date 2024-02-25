# Любую операцию с файлом можно разбить на три крупных этапа:
# 1.	Открытие файла
# 2.	Выполнение операции (запись, чтение)
# 3.	Закрытие файла
surname = 'Иванов'
f = open(r'fam.txt', 'w+', encoding='utf=8')
for i in range(1, 1001):
    if i % 100 == 0:
        f.write('\n')
    else:
        f.write(surname)
f.write('\n')
f.seek(0)

lines = ''
while True:
    line = f.readline()
    if not line:
        break
    line = line.strip().replace(surname, surname+'a', 100)
    print(line)
    lines = lines + '\n' + line

f.write(lines)
f.close()


