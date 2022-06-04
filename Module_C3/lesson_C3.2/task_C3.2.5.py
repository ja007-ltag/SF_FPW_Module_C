# Создать класс Square. Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.

class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException("Не верно указана сторона квадрата")
        else:
            self.a = a

    def __str__(self):
        return f"{self.a}"


sq1 = Square(5)
print(sq1)
sq2 = Square(-1)
