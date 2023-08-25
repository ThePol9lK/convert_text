import os
import time

from loader import bot, engine
from states.states import UserDocument
import textract


@bot.message_handler(commands=['voice'])
def handle_audio(message):
    bot.send_message(message.chat.id, 'Отправь мне файл')
    bot.set_state(message.from_user.id, UserDocument.enter_document)


@bot.message_handler(state=UserDocument.enter_document, content_types=['document'])
def process_file(message):
    document = message.document
    file_extension = document.file_name.rsplit('.', 1)[1].lower()

    if file_extension == 'docx':

        file_id = document.file_id
        file_data = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_data.file_path)

        try:

            temp_file_path = 'temp_file.' + file_extension
            with open(temp_file_path, 'wb') as f:
                f.write(downloaded_file)

            text = textract.process(temp_file_path).decode('utf-8')

            path_text = engine.check_dir(message.from_user.username, file_data.file_path.split('/')[-1].split('.')[0])
            engine.create_audio(text, path_text)

            with open(path_text, 'rb') as f:
                bot.send_voice(message.chat.id, voice=f.read())

        except Exception as e:

            bot.reply_to(message, 'Ошибка при чтении файла')

        finally:
        # Удаление временного файла
            os.remove(temp_file_path)

    elif file_extension == 'txt':
        file_info = bot.get_file(document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        try:
            text = downloaded_file.decode('utf-8')
            path_text = engine.check_dir(message.from_user.username, time.time())
            engine.create_audio(text, path_text)

            with open(path_text, 'rb') as f:
                bot.send_voice(message.chat.id, voice=f.read())

        except Exception as e:
            print(e)
            bot.reply_to(message, 'Ошибка при чтении файла')

    else:
        bot.reply_to(message, 'Неподдерживаемый тип файла')

