from config_data.config import PATH_AUDIO
from loader import bot
from states.states import UserDocument
from utils.engine import Engine


@bot.message_handler(commands=['voice'])
def handle_audio(message):
    bot.send_message(message.chat.id, 'Отправь мне файл')
    bot.set_state(message.from_user.id, UserDocument.enter_document)


@bot.message_handler(state=UserDocument.enter_document, content_types=['document'])
def process_file(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path).decode('UTF-8')
        Engine.auidoi(downloaded_file)

        # Отправляем голосовой ответ пользователю
        with open(PATH_AUDIO, 'rb') as f:
            bot.send_voice(message.chat.id, voice=f.read())

    except Exception as e:
        bot.reply_to(message, e)
