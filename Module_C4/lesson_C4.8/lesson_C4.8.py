# C4.8 Алгоритмы сортировки
# Наивная сортировка, так делать не нужно ни в коем случае!

import random  # для перемешивания массива

# пусть имеем массив всего лишь из 10 элементов
array = [2, 3, 1, 4, 6, 5, 9, 8, 7, 10]

is_sort = False  # станет True, если отсортирован
count = 0  # счетчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1

    random.shuffle(array)  # перемешиваем массив

    # проверяем отсортирован ли
    is_sort = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            is_sort = False
            break

print(array)
print(count)