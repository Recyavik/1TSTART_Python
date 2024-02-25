f = open(r"fam.txt", 'w+', encoding="utf=8")
for i in range(1, 10001):
    if i % 100 == 0:
        f.write("\n")
    else:
        f.write("Катаев")
f.write("\n")
f.seek(0)

lines = ""
while True:
    line = f.readline()
    if not line:
        break
    line = line.strip().replace("Катаев", "КатаевA", 100)
    print(line)
    lines = lines + "\n" + line
f.write(lines)
f.close()

