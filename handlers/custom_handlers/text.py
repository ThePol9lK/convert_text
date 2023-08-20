from loader import bot
from states.states import UserText
from utils.engine import Engine


@bot.message_handler(commands=['text'])
def handle_audio(message):
    bot.send_message(message.chat.id, 'Напиши мне сообщение, чтобы я его озвучил')
    bot.set_state(message.from_user.id, UserText.enter_text)


@bot.message_handler(state=UserText.enter_text, func=lambda message: True, content_types=['text'])
def process_file(message):
    try:

        text_from_user = message.text
        Engine.auidoi(text_from_user)

        # Отправляем голосовой ответ пользователю
        with open(PATH_AUDIO, 'rb') as f:
            bot.send_voice(message.chat.id, voice=f.read())

    except Exception as e:
        bot.reply_to(message, e)
