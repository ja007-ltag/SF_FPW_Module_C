# C4.5 Нелинейные структуры данных: графы и деревья.
# Деревья

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    # Поиск в глубину (depth-first search, DFS).
    # Префиксный подход обхода дерева
    def pre_order(self):
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:
            self.right_child.pre_order()

    # Поиск в глубину.
    # Постфиксный подход обхода дерева
    def post_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:
            self.right_child.post_order()

        print(self.value)  # процедура обработки

    # Поиск в глубину.
    # Инфиксный подход обхода дерева
    def in_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:
            self.right_child.in_order()


# создаем корень и его потомки /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

# Вызов pre_order()
print("pre_order")
node_root.pre_order()

# Вызов post_order()
print("post_order()")
node_root.post_order()

res = """2
5
11
6
7
4
9
5
2""".replace("\n", ", ")
print(res)
print("in_order")
node_root.in_order()
