from config_data.config import ADMIN_LIST
from loader import bot


@bot.message_handler(func=lambda message: str(message.from_user.id) not in ADMIN_LIST)
def handle_non_admin_message(message):
    # Обработка сообщений от неадминистраторов
    bot.reply_to(message, "Извините, только администраторы могут писать боту.")