# C3.4. Работа с файлами
# Видео с разбором работы с файловой системой

import os

test = os.path.join('C:\\', 'temp', '1', "temp.file")  # конкатенация путей (склеивание)
print(test)  # C:\temp\1\temp.file

test = os.path.join(os.getcwd(), "temp.file")
print(test)  # D:\Projects\PyCharm\SF_FPW_Module_C\Module_C3\lesson_C3.4\temp.file

test_path = os.getcwd()  # возвращает текущий путь
print(test_path)  # D:\Projects\PyCharm\SF_FPW_Module_C\Module_C3\lesson_C3.4

test = os.path.dirname(test_path)  # получить путь к каталогу, по заданному пути
print(test)  # D:\Projects\PyCharm\SF_FPW_Module_C\Module_C3

test = os.path.basename(test_path)  # имя файла/каталога по заданному пути (обрезает начало)
print(test)  # lesson_C3.4

test = os.path.normpath("tmp//2/../1/34\\54\\34/temp.file")  # нормализация пути
print(test)  # tmp\1\34\54\34\temp.file

test = os.path.exists(test_path)  # проверка существования пути
print(test)  # True

test = os.path.exists("D:\\Projects\\PyCharm\\SF_FPW_Module_C\\Module_C3\\lesson_C3.4\\temp.file")
print(test)  # False

test = os.listdir()  # Содержимое текущей или переданной директории
print(test)  # ['lesson_C3.4.py', 'lesson_C3.4_2.py', 'lesson_C3.4_3.py', 'task_3.4.3.py', 'test.txt']

test = os.listdir("D:\\Projects\\PyCharm\\SF_FPW_Module_C\\Module_C3")  # Содержимое текущей или переданной директории
print(test)  # ['lesson_C3.2', 'lesson_C3.3', 'lesson_C3.4']
