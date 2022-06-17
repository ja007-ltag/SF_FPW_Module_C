# C4.8 Алгоритмы сортировки
# Сортировка пузырьком

array = [10, 3, 1, 2, 4, 6, 5, 9, 8, 7]
print(array)
print("---------")

for i in range(len(array)):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
    print(array)

print("---------")
print(array)
