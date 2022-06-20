# Напишите программу, которая отправляет запрос на генерацию случайных текстов (используйте этот сервис:
# https://baconipsum.com/api/).
# Выведите первый из сгенерированных текстов.

import requests
import json

r = requests.get("https://baconipsum.com/api/?type=meat-and-filler")
print(r.status_code)
r = json.loads(r.content)
print(r[0])
