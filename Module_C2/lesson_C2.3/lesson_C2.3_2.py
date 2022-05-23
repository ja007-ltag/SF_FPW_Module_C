# Ну и напоследок стоит сказать пару слов о декораторе @classmethod.
# Который встречается довольно редко, ввиду его малой понятности для обывателей и синтаксической громоздкости.
#
# Используется он, как правило, чтобы открыть путь в полиморфизм (вспоминаем модуль C1,
# но если кратко — полиморфизм это разное поведение методов класса-родителя в классах-наследниках).

class ParentClass:
    @classmethod
    def method(cls, arg):
        print("%s classmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):
    @classmethod
    def call_original_method(cls):
        cls.method(6)


# Вызываем методы класса через класс.
ParentClass.method(0)  # ParentClassclassmethod. 0
ParentClass.call_original_method()  # ParentClassclassmethod. 5

ChildClass.method(0)  # ChildClassclassmethod. 0
ChildClass.call_original_method()  # ChildClassclassmethod. 6

# Вызываем методы класса через объект.
my_obj = ParentClass()
my_obj.method(1)  # ParentClassclassmethod. 1
my_obj.call_class_method()  # ParentClassclassmethod. 10


class A:
    @classmethod
    def method(cls):
        print(cls)


a = A()
a.method()
