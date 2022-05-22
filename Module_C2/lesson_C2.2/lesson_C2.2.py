# C2.2. Статические методы

class StaticClass:
    @staticmethod  # помечаем метод который мы хотим сделать статичным декоратором @staticmethod
    def GET_BAR():
        print("bar")


StaticClass.GET_BAR()
f = StaticClass()
f.GET_BAR()  # вызывать статические методы через объекты так же никто не запрещает
