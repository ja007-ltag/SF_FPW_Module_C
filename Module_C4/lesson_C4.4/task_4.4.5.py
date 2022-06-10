# Модифицируйте функцию проверки баланса скобок для двух видов скобок: круглых и квадратных.
#
# Для реализации такого алгоритма может быть полезным создание словаря,
# в котором закрывающая скобка — ключ, открывающая — значение.

def par_checker(string):
    stack = []  # инициализируем стек
    pars = {")": "(", "]": "[", "}": "{"}

    for s in string:
        if s in "([{":  # если открывающая скобка,
            stack.append(s)  # добавляем ее в стек
        elif s in ")]}":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()  # удаляем из стека
            else:
                return False

    return len(stack) == 0


s1 = "((a.kss)sdf((aasSdv )sdf( ssf()(sff -=-341))34134))(34134(1)2(3)123(2)32(3)2)"
print(par_checker(s1))
s1 = "(5+6)*(7+8)/(4+3)"
print(par_checker(s1))
s1 = "()(({ds123asd{sd-asd(aq=%^&!rf)123}41(24)}12[4])1)[]"
print(par_checker(s1))
s1 = "{srg;sdf';ld}([][])"
print(par_checker(s1))
