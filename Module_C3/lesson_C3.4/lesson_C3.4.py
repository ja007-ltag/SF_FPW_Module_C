# C3.4. Работа с файлами
# Путь к файлу

import os

# Получить текущий путь
start_path = os.getcwd()
print(start_path)

# Пробуем подняться на директорию выше
os.chdir("..")
print(os.getcwd())

# Теперь вернемся в ту директорию, из которой стартовали. Изначально мы сохраняли её в переменной start_path.
os.chdir(start_path)
print(os.getcwd())

# С помощью функции os.listdir() можно получить весь список файлов, находящихся в директории.
# Если не указать никаких аргументов, то будет взята текущая директория.

print(os.listdir("../lesson_C3.3"))

if "tmp.py" not in os.listdir():
    print("Файл 'tmp.py' отсутствует в данной директории")

if "lesson_C3.4.py" not in os.listdir():
    print("Файл 'lesson_C3.4.py' отсутствует в данной директории")
else:
    print("Файл 'lesson_C3.4.py' найден в данной директории")

# соединяет пути с учётом особенностей операционной системы
print(start_path)
print(os.path.join(start_path, 'test'))
