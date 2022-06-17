# C4.8 Алгоритмы сортировки
# Сортировка слиянием.  «Разделяй и властвуй»

array = [3, 2, 1, 10, 4, 6, 5, 9, 8, 7]
print(array)
print("---------")


def merge_sort(arr):  # «разделяй»
    if len(arr) < 2:
        return arr  # выходим из рекурсии
    else:
        middle = len(arr) // 2  # ищем середину
        left = merge_sort(arr[:middle])  # рекурсивно делим левую часть
        right = merge_sort(arr[middle:])  # и правую часть
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # «властвуй»
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


array = merge_sort(array)
print(array)

