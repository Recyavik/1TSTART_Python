f = open('Text.txt', 'r+', encoding='utf=8')
print(f.read())
print()
print(*f)
f.write('\nHi!')
f.writelines('\nПривет еще раз!')
print(f)

