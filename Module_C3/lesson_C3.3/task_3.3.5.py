#  Поэкспериментируйте с модулем time. Выведите в консоль текущее время, попробуйте вывести следующие данные:
#
# только время;
# только минуты;
# только дату;
# только месяц.

import time

# print('now is', time.strftime("%Y%m%d%h%M%S"))
print("Текущее время:", time.strftime("%H:%M.%S"))
print("Текущие минуты:", time.strftime("%M"))

print("Текущая дата:", time.strftime("%d %b %y"))
print("Текущая дата:", time.strftime("%d %B %Y"))
print("Текущая дата:", time.strftime("%d-%m-%y"))

print("Месяц:", time.strftime("%m"))
print("Месяц:", time.strftime("%b"))
print("Месяц:", time.strftime("%B"))
