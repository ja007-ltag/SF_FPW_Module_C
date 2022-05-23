# C2.3. Декораторы класса: @property, @classmethod. Ещё пару слов о нашей бывшей возлюбленной — инкапсуляции.

# @property очень классный декоратор, он-то, по сути, и обеспечивает нам прямой путь к инкапсуляции,
# позволяя объединить методы и поля.

class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # создадим свойство human_age, которое будет переводить возраст животного в человеческий
    @property
    def human_age(self):
        return self.age * 7.3

    # добавим новое поле - шкала счастья
    @property
    def happiness(self):
        return self._happiness

    # с помощью декоратора setter мы можем неявно передать во второй
    # аргумент значение, находящееся справа от равно, а не закидывать это
    # значение в скобки, как мы это делали в модуле C1, когда не знали о
    # декораторах класса
    @happiness.setter
    # допустим, мы хотим, чтобы счастье питомца измерялось шкалой от 0 до 100
    def happiness(self, value):
        if 0 <= value <= 100:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
# Т.к. метод помечен декоратором property, то нам не надо вызывать этот метод, чтобы получить результат
print(jane.human_age)
jane.happiness = 90
print(jane.happiness)
