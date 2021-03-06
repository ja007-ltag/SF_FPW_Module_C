# C3.2. Тонкости обработки исключений. Собственные классы исключений.

# Кстати говоря, класс с собственным исключением необязательно должен быть пустым.
# Если вы хотите добавить собственные аргументы в конструктор, дополнительно произвести какие-либо операции,
# то можете спокойно это делать, главное — не забыть о нескольких нюансах:
class ParentException(Exception):
    # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
    def __init__(self, message, error):
        super().__init__(message)  # помним про вызов конструктора родительского класса
        print(f"Errors: {error}")  # печатаем ошибку


class ChildException(ParentException):
    def __init__(self, message, error):
        super().__init__(message, error)


try:
    raise ChildException("Сообщение", "ОШИБКА!")  # поднимаем исключение-наследник, передаём дополнительный аргумент
except ChildException as e:
    print(e)  # выводим информацию об исключении
