# C3.5. Контекстные менеджеры. Ключевое слово with, принципы создания собственных контекстных менеджеров.

from datetime import datetime
import time
from contextlib import contextmanager


class Timer:
    def __init__(self):
        pass

    def __enter__(self):  # для запуска контекстного менеджера
        self.start = datetime.utcnow()
        return object  # если требуется отдельный объект

    def __exit__(self, exc_type, exc_val, exc_tb):  # после запуска контекстного менеджера, в переменные попадает ошибка
        print(f'Time passed: {(datetime.utcnow() - self.start).total_seconds()}')


@contextmanager  # требуется библиотека contextmanager
def timer():
    start = datetime.utcnow()
    yield object  # если не нужен объект, то просто пишем yield
    print(f'Time passed: {(datetime.utcnow() - start).total_seconds()}')


with Timer() as name_object1:
    # name_object1  # Производим действия с объектом
    time.sleep(2)

with timer() as name_object2:
    time.sleep(3)
