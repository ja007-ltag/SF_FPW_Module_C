# C4.8 Алгоритмы сортировки
# Быстрая сортировка

array_1 = [3, 2, 1, 4, 10, 6, 5, 9, 8, 7]
print(array_1)
print("---------")


def qsort(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

    return array


print("---------")
array_1 = qsort(array_1)
print(array_1)
