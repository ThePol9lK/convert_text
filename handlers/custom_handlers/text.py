from telebot.types import Message

import time

from loader import bot, engine
from states.states import UserText


@bot.message_handler(commands=['text'])
def handle_audio(message: Message):
    """
    Обработка команды text
    :param message: Message
    :return:
    """
    bot.send_message(message.chat.id, 'Напиши мне сообщение, чтобы я его озвучил')
    bot.set_state(message.from_user.id, UserText.enter_text)


@bot.message_handler(state=UserText.enter_text, func=lambda message: True, content_types=['text'])
def process_file(message: Message):
    """
    Проверка текста и ее последующая обработка
    :param message: Message
    :return:
    """
    try:

        text_from_user = message.text
        path_text = engine.check_dir(message.from_user.username, time.time())
        engine.create_audio(text_from_user, path_text)

        with open(path_text, 'rb') as f:
            bot.send_voice(message.chat.id, voice=f.read())

    except Exception as e:
        bot.reply_to(message, e)
