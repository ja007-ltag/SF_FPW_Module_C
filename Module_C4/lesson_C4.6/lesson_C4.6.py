# C4.6 Создание собственных структур

# Сейчас мы попробуем создать класс LinkedList, реализующий список.
# Элементы списка будут представлять собой экземпляры класса Node.

class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None  # ссылка на первый элемент
        self.last = None  # ссылка на последний элемент

    def clear(self):  # очищаем список
        self.__init__()

    def __str__(self):  # функция печати
        res = ""

        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            res += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует, добавляем пробел
                res += " "

        return res

    def push_left(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def push_right(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    # удаление первого элемента
    def pop_left(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список имеет только один элемент
            node = self.first  # сохраняем его
            self.clear()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    # удаление последнего элемента
    def pop_right(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список имеет только один элемент
            node = self.first  # сохраняем его
            self.clear()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний элемент
            pointer = self.first  # создаем указатель (берем первый указатель в списке)

            while pointer.next is not node:  # пока следующий указатель существует (ищем предпоследний элемент)
                pointer = pointer.next  # переходим к следующему указателю

            pointer.next = None  # обнуляем указатель, в последнем элементе, чтобы
            self.last = pointer  # предпоследний стал последним
            return node

    def __iter__(self):  # Объявляем класс как итератор
        self.current = self.first  # в текущий элемент помечаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход на следующий элемент
            return node  # возвращаем текущий элемент

    def __len__(self):  # «магический» метод, возвращающий размер структуры данных
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count


LL = LinkedList()

LL.push_right(1)
print(LL)
LL.push_left(2)
print(LL)
LL.push_right(3)
print(LL)
print(LL.pop_right(), 'удален')
print(LL)
LL.push_left(4)
print(LL)
LL.push_right(5)
print(LL)
print(LL.pop_left(), 'удален')
print(LL)
print('---------')
print(LL.first, LL.last)

print(len(LL))
for i in LL:
    print(i)
