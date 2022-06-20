# C5.2 Библиотека Requests и её лучший друг JSON
# попробуем отправить POST-запрос

import requests
import json

data = {"key": 'value'}

# отправляем пост-запрос, но только в этот раз тип передаваемых данных будет JSON
r = requests.post("https://httpbin.org/post", json=json.dumps(data))
print(r.status_code)
out = json.loads(r.content)
print(type(out))
print()

for key, value in out.items():
    print(f'{key} : {value}')
