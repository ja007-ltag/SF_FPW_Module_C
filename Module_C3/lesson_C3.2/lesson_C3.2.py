# C3.2. Тонкости обработки исключений. Собственные классы исключений.

try:
    raise ZeroDivisionError  # возбуждаем исключение ZeroDivisionError
except ArithmeticError:  # ловим его родителя
    print("Hello from arithmetic error")

try:
    x = 1
except BaseException as e:
    print("Error:", e)

print()

try:
    raise ZeroDivisionError("ААААА, не умею делить на ноль!!!")
except ZeroDivisionError as e:  # сначала пытаемся поймать наследника
    print("Zero Division Error:", e)
except ArithmeticError as e:  # потом ловим родителя
    print("Arithmetic Error:", e)
