"""
Базовый обработчик сообщений: выводит сообщение-помощник с существующими командами
"""

from loader import bot
from telebot.types import Message

@bot.message_handler(commands=['help'])
def get_help(message: Message) -> None:
    """
    ВЫВОД для команда help
    :param message:
    :return:
    """
    bot.send_message(message.chat.id, 'Я умею конвертировать тексты и файлы в формат mp3')
