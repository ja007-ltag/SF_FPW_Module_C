# C3.4. Работа с файлами
# Видео с разбором работы с файловой системой и файлами (продолжение)

f = open("test_video.txt", "w", encoding="utf=8")

print(f.tell())  # проверка указателя на текущую позицию

print("Записано", f.write("This is a test string\n"), "символов.")
print(f.tell())
f.flush()  # записывает данные на диск

print("Записано", f.write("This is a new string\n"), "символов.")
f.flush()
print(f.tell())

f.close()

print("---------")

f = open("test_video.txt", "r", encoding="utf=8")

print(f.tell())
print(f.read(23))
print(f.tell())

print(f.seek(1))
print(f.tell())
print(f.read())

f.close()

print("---------")

# Открываем на до запись
f = open("test_video.txt", "a", encoding="utf8")

sequence = ["ocher string\n", "123\n", "test test\n"]
f.writelines(sequence)

f.close()

f = open("test_video.txt", "r", encoding="utf8")

print(f.readlines())

f.close()

print("---------")

# Метод f.readline() возвращает строку (символы от текущей позиции до символа переноса строки):
f = open("test_video.txt", "r", encoding="utf8")

print(f.readline(), end='')
print(f.read(4))
print(f.readline(), end='')

f.close()

print("---------")

f = open("test_video.txt", "r", encoding="utf8")

for line in f:
    print(line.strip())

f.close()

print("---------")

f = open("test_video.txt", "r", encoding="utf8")

print(iter(f))
print(id(f) == id(iter(f)))

f.close()

print("---------")

with open("test_video.txt", "rb") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

f.readline()
