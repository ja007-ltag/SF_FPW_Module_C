# Очередь

# Создадим класс Queue - нужная нам очередь
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализация пустого списка
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди

    # Наличие элементов в очереди
    def is_empty(self):  # очередь пустая?
        # да, если указатели совпадают и в них содержится 0
        return self.head == self.tail and self.tasks[self.head] == 0

    def size(self):
        if self.head == self.tail:
            if self.is_empty():  # если очередь пуста
                return 0
            else:
                return self.max_size
        else:
            if self.head < self.tail:
                return self.tail - self.head
            else:
                return self.max_size - self.head + self.tail

    def add(self):
        self.task_num += 1  # увеличиваем порядковый номер задачи
        self.tasks[self.tail] = self.task_num  # добавляем его в очередь
        print(f"Задача №{self.tasks[self.tail]} добавлена")

        # увеличиваем указатель на 1 по модулю максимального числа элементов для зацикливания очереди в списке
        self.tail = (self.tail + 1) % self.max_size

    def show(self):  # выводим приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} в приоритете")

    def do(self):
        print(f"Задача №{self.tasks[self.head]} выполнена")
        self.tasks[self.head] = 0
        self.head = (self.head + 1) % self.max_size
        pass


size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду: ")

    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")

    elif cmd == "size":
        print("Количество задач в очереди:", q.size())

    elif cmd == "add":
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")

    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()

    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()

    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break

    else:
        print("Введена не верная команда")
