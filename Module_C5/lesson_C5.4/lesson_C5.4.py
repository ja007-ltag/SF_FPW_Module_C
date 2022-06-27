# C5.4 Парсинг данных с сайтов с помощью lxml

import requests
import lxml.html
# from lxml import etree

html = requests.get("https://www.python.org/").content  # получим html главной странички официального сайта python

tree = lxml.html.document_fromstring(html)

# Забираем текст тега <title> из тега <head>, который лежит в свою очередь внутри тега <html>
# (в этом невидимом теге <head> у нас хранится основная информация о страничке.
# Её название и инструкции по отображению в браузере.)
title = tree.xpath("/html/head/title/text()")

print(title)
