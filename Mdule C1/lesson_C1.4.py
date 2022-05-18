# Классы

class User:
    number_of_finger = 5
    number_of_eyes = 2


peter = User()
peter.name = "Peter Robertson"

julia = User()
julia.name = "Julia Donaldson"

print(type(peter), type(peter.name), peter.name)
print(type(julia), type(julia.name), julia.name)

peter.email = "peterrobertson@mail.com"
print(peter.email)
print()

lancelot = User()
print(lancelot.number_of_finger)
