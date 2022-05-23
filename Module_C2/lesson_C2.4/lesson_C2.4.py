# C2.4. Исключения

try:
    print("Перед исключением")

    c = 3 / 0
    print(c)  # печатаем c = a / b если всё хорошо
except ZeroDivisionError as e:
    print("После исключения. Поймали ошибку в except")
else:  # код выполняется только в том случае, если не вылетело никакого исключения.
    print("Ошибок не было попали в else")
finally:  # код в блоке выполнится в любом случае, при выходе из try-except
    print("Код в finally, должен выполниться в любом случае")

print("Код в самом конце")
print()

try:
    age = 100

    if not (0 <= age < 100):
        raise ValueError("Тебе не может быть столько лет")

    print(f"Тебе {age} лет!")
except ValueError:
    print("Неправильный возраст")
