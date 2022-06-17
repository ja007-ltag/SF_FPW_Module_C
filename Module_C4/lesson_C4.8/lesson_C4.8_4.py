# C4.8 Алгоритмы сортировки
# Сортировка вставками

array = [3, 2, 1, 10, 4, 6, 5, 9, 8, 7]
print(array)
print("---------")

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x

print("---------")
print(array)

