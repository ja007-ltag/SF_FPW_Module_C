# C4.7 Алгоритмы поиска

def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


def count(array, element):
    cnt = 0
    for i, a in enumerate(array):
        if a == element:
            cnt += 1
    return cnt


# алгоритм двоичного поиска
def binary_search(array, element, left=0, right=None):
    if right is None:
        right = len(array)

    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (left + right) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


# array1 = list(map(int, "6 3 8 9 34 3 32 33 32 3 3".split()))
# element1 = int("66")
#
# print(find(array1, element1))
# print(count(array1, element1))

element1 = 66
array1 = [i for i in range(1, 100)]
print(array1[binary_search(array1, element1)])
