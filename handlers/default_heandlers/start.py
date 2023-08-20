from telebot.types import Message

from keyboards.inline.choise_kb import choise
from loader import bot


@bot.message_handler(commands=['start'])
def get_start(message: Message) -> None:
    """
    ВЫВОД для команда start
    :param message:
    :return:
    """
    bot.send_message(message.chat.id, 'Привет, я бот для конвертации из текста в голос', reply_markup=choise())
