from telebot.types import Message
from loader import bot

#Обработка команды start
@bot.message_handler(commands=['start'])
def get_start(message: Message) -> None:
    """
    ВЫВОД для команда start
    :param message:
    :return:
    """
    bot.send_message(message.chat.id, 'Привет, я бот для конвертации из текста в голос')