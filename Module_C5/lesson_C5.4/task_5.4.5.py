# Используя полученные знания, допишите сделанный в начале юнита скрипт
# (где мы доставали заголовки новостей о Python с Python.org) так, чтобы он показывал ещё и дату добавления новости.
#
# Примечание: Для получения атрибутов тега (т.е. его дополнительных параметров) используется метод .get(<имя атрибута>).

import requests
import lxml.html
# from lxml import etree

# получим html главной странички официального сайта python
html = requests.get('https://www.python.org/').content

# Создадим объект ElementTree. Он возвращается функцией parse()
tree = lxml.html.document_fromstring(html)

# Помещаем в аргумент метода findall скопированный xpath. (в пути удален первый тег html)
ul = tree.xpath("/html/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li")

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find("a")
    time = li.find("time")
    print(time.get("datetime"), a.text)
