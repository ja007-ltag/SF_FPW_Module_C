# C4.4 Основные структуры данных: список, стек, очередь

# Напишем функцию par_checker(string), которая проверяет строку string на корректность расстановки скобок.

def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем ее в стек
        elif s == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:
                return False

    return len(stack) == 0


s1 = "((a.ksf3jh3as)sdf((as4ee5fv )sdf( s3dfs1f()(sdf2fs -=-341))34134))(34134(1)2(3)123(2)32(3)2)"
print(par_checker(s1))
s1 = "(5+6)*(7+8)/(4+3)"
print(par_checker(s1))
