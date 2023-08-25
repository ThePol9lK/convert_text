"""
Подключение к боту с помощью токена
"""

from telebot import TeleBot
from config_data.config import *
from telebot.storage import StateMemoryStorage

from utils.engine import Engine

storage = StateMemoryStorage()
bot = TeleBot(token=BOT_TOKEN, state_storage=storage)
engine = Engine()