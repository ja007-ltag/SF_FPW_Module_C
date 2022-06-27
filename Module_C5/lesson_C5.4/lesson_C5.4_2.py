# C5.4 Парсинг данных с сайтов с помощью lxml

# import requests
import lxml.html
from lxml import etree

# попытаемся спарсить наш файл с помощью html-парсера
tree = etree.parse("Welcome to Python.org.html", lxml.html.HTMLParser())

# Помещаем в аргумент метода findall скопированный xpath. (в пути удален первый тег html)
# Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
# *можно обоими вариантами*
# ul = tree.findall("/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li")
ul = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li')


# //*[@id="content"] /div/section/div[2]/div[1]/div/ul/li[1]
# /html/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li[1]

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    # В каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка,
    # на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
    a = li.find("a")

    print(a.text)  # из этого тега забираем текст, это и будет нашим названием
