# C5.3 Создание Telegram-бота

import telebot

with open("token_bot", "r", encoding="utf8") as f:
    TOKEN = f.readline().strip()

bot = telebot.TeleBot(TOKEN)  # создать объект bot, используя токен, полученный при регистрации бота


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=["start", "help"])
def handle_start_help(message):
    if message.chat.username is None:
        bot.send_message(message.chat.id, f"Приветствую тебя странствующий незнакомец, с не заданным username!")
    else:
        bot.send_message(message.chat.id, f"Приветствую тебя странствующий {message.chat.username}!")

    print(f"{message.text}, {message.chat.username}, {message.chat.first_name} {message.chat.last_name}")
    if "help" in message.text:
        if message.chat.first_name is None:
            bot.reply_to(message, f"Почему у тебя не задан first_name?\n"
                                  f"Что вас беспокоит, {message.chat.last_name}?\n"
                                  f"Существо без first_name...")
        elif message.chat.last_name is None:
            bot.reply_to(message, f"Почему у тебя не задан last_name?\n"
                                  f"Что вас беспокоит, {message.chat.first_name}?\n"
                                  f"Существо без last_name?...")
        else:
            bot.reply_to(message, f"Что вас беспокоит, {message.chat.first_name} {message.chat.last_name}?")


# Обрабатывается любой текст
@bot.message_handler(content_types=["text"])
def handle_docs_audio(message):
    print(f"{message.text}, {message.chat.username}, {message.chat.first_name} {message.chat.last_name}")
    bot.reply_to(message, f"Прости меня великий {message.chat.first_name}!\n"
                          f"Меня создал глупый Легендарный Тигр, и я ничего не умею...")


# Обрабатывается фото
@bot.message_handler(content_types=["photo"])
def handle_docs_audio(message):
    print(f"{message}, {message.chat.username}, {message.chat.first_name} {message.chat.last_name}")
    bot.reply_to(message, f"Классная картинка XDD")
    pass


# Чтобы запустить бота, нужно воспользоваться методом polling
bot.polling(none_stop=True)  # none_stop=True - бот должен стараться не прекращать работу при возникновении ошибок
