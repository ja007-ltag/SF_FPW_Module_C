# Создать вычисляемое свойство для класса Square. Сделайте метод по вычислению площади свойством.
# Сделайте сторону квадрата свойством, которое можно установить только через сеттер.
# В сеттере добавьте проверку условия, что сторона должна быть неотрицательной.

class Square:
    def __init__(self, a):
        self._a = a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value

    @property
    def area(self):
        return self._a ** 2


sq_1 = Square(3)
sq_1.a = 7
print(sq_1.a)
print(sq_1.area)
