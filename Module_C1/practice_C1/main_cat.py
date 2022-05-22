from cat import Cat

cat_1 = Cat(name="Сaм", gender="boy", age=2)
cat_2 = Cat(name="Baron", gender="boy", age=2)

print(f"Name: {cat_1.get_name()}, gender: {cat_1.get_gender()}, age: {cat_1.get_age()}")
print(f"Name: {cat_2.get_name()}, gender: {cat_2.get_gender()}, age: {cat_2.get_age()}")


class Dog(Cat):
    def get_pet(self):
        return self.name, self.age


dog_1 = Dog("Mukhtar", "boy", 0)
dog_2 = Dog("Felix", "boy", 2)

print(*dog_1.get_pet())
print(*dog_2.get_pet())
