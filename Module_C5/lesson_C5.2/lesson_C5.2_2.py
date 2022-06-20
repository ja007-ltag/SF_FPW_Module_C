# C5.2 Библиотека Requests и её лучший друг JSON

import requests
import json

r = requests.get("https://api.github.com")
print(r.status_code)
print(type(r))
d = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы

print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений
