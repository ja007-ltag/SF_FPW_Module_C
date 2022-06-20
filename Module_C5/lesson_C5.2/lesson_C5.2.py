# C5.2 Библиотека Requests и её лучший друг JSON

import requests
import json

# # делаем запрос на сервер по переданному адресу
# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# print(r.status_code)
# print(r.content)

# попробуем поймать json-ответ
r = requests.get("https://baconipsum.com/api/?type=meat-and-filler")
print(r.status_code)

texts = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы
print(type(texts))

for text in texts:
    print(text[:100], '\n')
