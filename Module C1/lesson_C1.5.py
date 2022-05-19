# C1.5. Магический метод __init__

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")

print(peter.name, peter.email)
print(julia.name, julia.email)
