from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def choise() -> InlineKeyboardMarkup:
    """
    Клавиатура для inline кнопок
    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    keyboard = InlineKeyboardMarkup()
    key_fails = InlineKeyboardButton(text='Файл', callback_data='key_fails')
    key_text = InlineKeyboardButton(text='Текст', callback_data='key_text')
    keyboard.add(key_fails, key_text)
    return keyboard
