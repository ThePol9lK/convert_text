import handlers
from loader import bot
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_bot_commands


if __name__ == '__main__':

    bot.add_custom_filter(StateFilter(bot))
    set_bot_commands(bot)
    bot.infinity_polling(skip_pending=True)
