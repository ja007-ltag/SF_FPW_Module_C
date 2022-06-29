# Напишите программу, которая будет записывать и кэшировать номера телефонов ваших друзей.
#
# Программа должна уметь воспринимать несколько команд:
#
# записать номер;
# показать номер друга в консоли при вводе имени;
# удалить номер друга по имени.
# Кэширование надо производить с помощью Redis. Ввод и вывод информации должен быть реализован через консоль
# (с помощью функций input() и print()).

import redis

red = redis.Redis(
    host="",
    port=0,
    password=""
)

cont = True

while cont:
    action = input("Action:\t")

    if action == "write":
        name = input("Name: ")
        phone = input("Phone: ")
        status = red.set(name, phone)
        if status:
            print("Successfully completed\n")
        else:
            print("Error!!!\n")

    elif action == "read":
        name = input("Name: ")
        phone = red.get(name)
        if phone:
            print(f"{name} phone is {str(phone)}\n")
        else:
            print(f"User {name} not found\n")

    elif action == "delete":
        name = input("Name: ")
        phone = red.delete(name)
        if phone:
            print(f"{name} phone is deleted\n")
        else:
            print(f"User {name} not found\n")

    elif action == "exit":
        cont = False

    else:
        print("Invalid command entered\n")
