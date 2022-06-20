import timeit

# Алгоритм Евклида (нахождение НОД)
a = 50
b = 130
while a and b:
    if a > b:
        a %= b
    else:
        b %= a
# print(a+b)


# Алгоритм бинарного поиска
def binary_search(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while first <= last and index == -1:
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid -1
            else:
                first = mid + 1
    return index


print(binary_search([10, 20, 30, 40, 50], 20))
print((timeit.timeit("binary_search([1, 4, 5, 6, 7, 10, 20, 30, 40, 50], 20)",
                     setup="from __main__ import binary_search", number=10000)))


# Алгоритм бинарного поиска (рекурсивный)
def recursive_binary_search(arr, target):
    mid = len(arr) // 2
    if len(arr) == 1:
        return mid
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] < target:
            callback_response = recursive_binary_search(arr[mid:], target)
            return mid + callback_response
        else:
            return recursive_binary_search(arr[:mid], target)


print(recursive_binary_search([10, 20, 30, 40, 50], 200))
print((timeit.timeit("recursive_binary_search([1, 4, 5, 6, 7, 10, 20, 30, 40, 50], 20)",
                     setup="from __main__ import recursive_binary_search", number=10000)))
