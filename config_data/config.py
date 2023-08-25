"""
Конфигурация бота. Объявление токена и стандартных команд.
"""

import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены: отсутствует файл .env')

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_LIST = os.getenv('ADMINS')

DEFAULT_COMMANDS = (
    ('help', 'Помощь'),
    ('start', 'Запустить бот'),
)

CUSTOM_COMMANDS = (
    ('voice', 'Ковертация файла в mp3'),
    ('text', 'Ковертация текста в mp3'),
)
