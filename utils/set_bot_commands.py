"""
Выводит базовые команды в меню
"""

from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS, CUSTOM_COMMANDS


def set_bot_commands(bot):
    bot.set_my_commands(
        (BotCommand(*i) for i in CUSTOM_COMMANDS + DEFAULT_COMMANDS)
    )
