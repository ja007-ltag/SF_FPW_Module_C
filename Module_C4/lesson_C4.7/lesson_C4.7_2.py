# C4.7 Алгоритмы поиска
# Двоичное дерево поиска

# Какие методы должен реализовать этот класс?
# 1. Поиск элемента
# 2. Поиск минимума/максимума
# 3. Поиск следующего элемента
# 4. Вставка элемента
# 5. Удаление элемента
# 6. Построение дерева по массиву

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):  # печать с помощью обхода в ширину
        queue = [self]  # создаем очередь
        values = []  # значения в порядке обхода в ширину
        while queue:  # пока очередь не пустая
            last = queue.pop(0)  # извлекаем из начала
            if last is not None:
                values.append("%d" % last.value)  # добавляем значение
                queue.append(last.left_child)  # добавляем левого потомка
                queue.append(last.right_child)  # добавляем правого потомка
        return ' '.join(values)

    def search(self, x):
        if self.value == x:  # если нашли элемент,
            return self  # возвращаем ссылку на узел
        elif x < self.value:  # или, если значение меньше ключа, рекурсивно
            return self.left_child.search(x)  # ищем в левом поддереве
        elif x > self.value:
            return self.right_child.search(x)
        else:  # если не нашли значение
            return False

    def minimum(self):
        if self.left_child is None:
            return self
        else:
            return self.left_child.minimum()

    def maximum(self):
        if self.right_child is None:
            return self
        else:
            return self.right_child.maximum()

    def next_value(self, x):
        current = self
        successor = None
        while current is not None:
            if current.value > x:
                successor = current
                current = current.left_child
            else:
                current = current.right_child
        return successor

    def prev_value(self, x):
        current = self
        successor = None
        while current is not None:
            if current. value < x:
                successor = current
                current = current.right_child
            else:
                current = current.left_child
        return successor

    def insert(self, x):
        if x > self.value:  # идем в правое поддерево
            if self.right_child is not None:  # если оно существует,
                self.right_child.insert(x)  # делаем рекурсивный вызов
            else:  # иначе создаем правого потомка
                self.right_child = BinarySearchTree(x)
        else:  # иначе в левое поддерево и делаем аналогичные действия
            if self.left_child is not None:
                self.left_child.insert(x)
            else:
                self.left_child = BinarySearchTree(x)
        return self  # возвращаем корень

    def delete(self, x):
        # первым этапом мы должны найти удаляемый узел и его предка
        parent = self  # родитель
        node = self
        if not self.search(x):  # узла с таким значение не существует
            return self
        while node.value != x:
            parent = node
            if parent.left_child is not None and x < parent.value:
                node = parent.left_child
            elif parent.right_child is not None and x > parent.value:
                node = parent.right_child
        # по завершении в node хранится искомый узел

        # первый случай - если лист
        if node.left_child is None and node.right_child is None:
            if parent.left_child is node:  # если родитель является левым
                parent.left_child = None
            if parent.right_child is node:
                parent.right_child = None
            if parent.value == x:
                # если нет листов и parent == node до сих пор,
                # значит, нужно вернуть None для корректной работы рекурсии
                return None

        # второй случай - имеем одного потомка
        elif node.left_child is None or node.right_child is None:
            if node.left_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.left_child
                elif parent.right_child is node:
                    parent.right_child = node.left_child
            if node.right_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.right_child
                elif parent.right_child is node:
                    parent.right_child = node.right_child

        else:  # третий случай - имеем двух потомков
            next_value = node.next_value(x).value  # ищем следующее значение
            node.value = next_value  # меняем на него
            # далее рекурсивный вызов
            node.right_child = node.right_child.delete(next_value)
        return self


BinSTree_1 = BinarySearchTree(25)
list_value = [10, 15, 37, 30, 65]
for val in list_value:
    BinSTree_1.insert(val)

BinSTree_1.delete(37)
print(BinSTree_1)
BinSTree_1.delete(25)
print(BinSTree_1)
