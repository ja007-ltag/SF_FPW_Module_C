# C4.8 Алгоритмы сортировки
# Сортировка выбором

array = [2, 3, 1, 10, 4, 6, 5, 9, 8, 7]
print(array)

count = 0
for i in range(len(array)-1):
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i+1, len(array)):
        count += 1
        if array[j] < array[idx_min]:
            idx_min = j

    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)

# сортировка убыванием
for i in range(len(array)-1):
    idx_max = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i+1, len(array)):
        if array[j] > array[idx_max]:
            idx_max = j

    if i != idx_max:
        array[i], array[idx_max] = array[idx_max], array[i]

print(array)
print(count)
