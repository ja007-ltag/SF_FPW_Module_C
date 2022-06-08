# Напишите контекстный менеджер, который умеет безопасно работать с файлами.
#
# В конструктор объекта контекстного менеджера передаются два аргумента: первый — путь к файлу,
# который надо открыть, второй — тип открываемого файла (для записи, для чтения и т. д.).
#
# При входе в контекстный менеджер, должен открываться файл, и возвращаться объект для работы с этим файлом.
#
# При выходе из контекстного менеджера файл должен закрываться.
# (Эталоном работы можно считать контекстный менеджер open).

from contextlib import contextmanager


class OpenFile:
    def __init__(self, path, mode):
        self.file = open(path, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager
def open_file(path, mode):
    file = open(path, mode)
    yield file
    file.close()


with OpenFile("test.txt", "wt") as f:
    f.write("Этот менеджер, работает как менеджер\n")
    f.write("Запишем ещё что-нибудь\n")
    f.write("+1 строка\n")

with open_file("test.txt", "rt") as f:
    for line in f.readlines():
        print(line.strip())
