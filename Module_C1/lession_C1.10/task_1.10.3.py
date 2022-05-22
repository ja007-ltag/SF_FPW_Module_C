# Задание 1.10.3
# В проекте «Дом питомца» добавим новую услугу — электронный кошелек.
# Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.
#
# Далее сделайте вывод о клиентах в консоль в формате:
#
# «Иван Петров. Москва. Баланс: 50 руб.»

# Задание 1.10.4
# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
#
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Customers:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'«{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.»'

    def get_guest(self):
        return f'«{self.name} {self.surname}. {self.city}.»'


customer_1 = Customers("Иван", "Петров", "Москва", 500)
customer_2 = Customers("Сидр", "Иванович", "Рязань", 150)
customer_3 = Customers("Пётр", "Егорович", "Минск", 250)
customer_4 = Customers("Анна", "Ивановна", "Дмитров", 100)
customer_5 = Customers("Елена", "Антоновна", "Ногинск", 50)
print(customer_1)

guest_list = [customer_1, customer_2, customer_3, customer_4, customer_5]
for person in guest_list:
    print(person.get_guest())
