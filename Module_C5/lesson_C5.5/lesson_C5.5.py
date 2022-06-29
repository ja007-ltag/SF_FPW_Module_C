# С5.5 Кэширование с помощью Redis
# Добавление и считывание данных

import redis
import json

red = redis.Redis(
    host="", # Ваш хост, если вы поставили Редис к себе на локальную
    # машину, то у вас это будет localhost. Если же вы находитесь на Windows,
    # то воспользуйтесь полем host из вашей облачной БД.

    port=0,  # Порт подключения. На локальной машине это должно быть 6379.
    # Для пользователей облачного сервиса порт всегда разный, поэтому его надо копировать оттуда же, что и host.

    password=""  # Для локальной машины пароль не требуется (если вы устанавливали Редис
    # к себе на компьютер).
    # Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password
)

red.set('var1', 'value1')
print(red.get('var1'))

dict1 = {'key1': 'value1', 'key2': 'value2'}  # словарь для записи
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
get_dict = json.loads(red.get('dict1'))  # с помощью loads() превращаем данные, полученные из кэша обратно в словарь
print(type(get_dict))  # убеждаемся, что мы получили действительно словарь
print(get_dict)  # и выводим его содержание