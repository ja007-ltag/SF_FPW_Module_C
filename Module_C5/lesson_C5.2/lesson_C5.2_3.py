# C5.2 Библиотека Requests и её лучший друг JSON
# попробуем отправить POST-запрос

import requests
import json

r = requests.post("https://httpbin.org/post", data={"key": "value"})  # отправляем пост-запрос
print(r.status_code)
out = json.loads(r.content)
print(type(out))
print()

for key, value in out.items():
    print(f'{key} : {value}')
