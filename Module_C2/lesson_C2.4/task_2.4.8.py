# Создать скрипт, который будет в input() принимать строки, и их необходимо будет конвертировать в числа,
# добавить try-except на то, чтобы строки могли быть с конвертированы в числа.
#
# В случае удачного выполнения скрипта написать: «Вы ввели правильное число».
#
# В конце скрипта обязательно написать: «Выход из программы».
#
# ПРИМЕЧАНИЕ: Для отлова ошибок используйте try-except, а также блоки finally и else.

try:
    var = int(input("Введите число: "))
except ValueError as e:
    print("Вы ввели не правильное число")
else:
    print("Вы ввели", var)
finally:
    print("Выход из программы")