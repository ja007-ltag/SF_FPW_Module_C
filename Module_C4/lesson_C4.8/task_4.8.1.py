# Найдите количество цифр в записи числа 100! (факториал от 100).

def factorial(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res


n = 100000
f_100 = factorial(n)
print(f"Количество цифр в записи числа {n}! = {len(str(f_100))}")