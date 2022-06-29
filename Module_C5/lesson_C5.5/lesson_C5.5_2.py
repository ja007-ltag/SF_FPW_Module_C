# С5.5 Кэширование с помощью Redis
# Удаление данных из Redis

import redis
# import json

red = redis.Redis(
    host="",
    port=0,
    password=""
)

red.delete('var1')
red.delete('dict1')

print(red.get("var1"))
print(red.get("dict1"))
