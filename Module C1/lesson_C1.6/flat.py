class Room1:
    def get_room(self):
        print("room1")


class Room2:
    def get_room(self):
        print("room2")

    def get_room2(self):
        print("room2 for flat")


class Kitchen:
    def get_kitchen(self):
        print("kitchen")


class Flat(Kitchen, Room1, Room2):
    pass


f = Flat()
f.get_kitchen()
f.get_room()
f.get_room2()

print(isinstance(f, Flat))
print(isinstance(f, Room1))
print(isinstance(f, Room2))
print("---------------")


class RoomB1:
    def get_room(self):
        print("room_b1")


class RoomB2:
    def get_room(self):
        print("room_b2")


class RoomB3:
    def get_room(self):
        print("room_b3")


class Flat(RoomB2, RoomB3):
    pass


print(Flat.mro())  # метод класса, который показывает порядок наследования

f_b = Flat()
f_b.get_room()
