from bs4 import BeautifulSoup
import requests

# выносим базовую ссылку в отдельную переменную
base = "https://ru.stackoverflow.com"

# получаем код html с помощью библиотеки requests
html = requests.get(base).content

# Создаем объект супа. 1-ый аргумент - весь html, 2-ой - сама библиотека для парсинга. В нашем случае lxml
soup = BeautifulSoup(html, "lxml")

# находим с помощью метода find() нужный нам див, уточняя id
div = soup.find('div', id="question-mini-list")

# Ищем только нужные нам объекты, в которых есть интересующий нас тег <a>
h3 = div.find_all("h3")

for el in h3:
    a = el.find("a")
    # Метод getText() возвращает текст внутри тега.
    # Чтобы получить атрибут тега (ссылка лежит в атрибуте href) можно обратиться к нему как к словарю через []
    # или же использовать метод get()
    print(a.getText(), base + a.get('href'))  # печатаем название вопроса и ссылку на него
    print()

    # если нужно найти родительский тег, можно воспользоваться методом find_parent()
    parent = a.find_parent()
    print(parent)  # Получаем тег родитель. На момент написания это был тег <h3>
    print("---")
