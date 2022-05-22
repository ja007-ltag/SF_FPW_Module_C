# Задание на самопроверку.
#
# Напишите класс SquareFactory с одним статическим методом, принимающим единственный аргумент — сторону квадрата.
# Данный метод должен возвращать объект класса Square с переданной стороной.

class Square:
    def __init__(self, a):
        self.a = a


class SquareFactory:
    @staticmethod
    def create_square(side):
        return Square(side)


sq1 = SquareFactory.create_square(5)
print(sq1.a)
