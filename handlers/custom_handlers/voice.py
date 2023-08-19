import pyttsx3
from loader import bot
from states.states import UserInfoState


@bot.message_handler(commands=['voice'])
def handle_audio(message):
    bot.send_message(message.chat.id, 'Отправь мне файл')
    bot.set_state(message.from_user.id, UserInfoState.enter_text)


@bot.message_handler(state=UserInfoState.enter_text, content_types=['document'])
def process_file(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # file_extension = file_info.file_path.rsplit('.', 1)[1].lower()
        #
        # if file_extension in ['txt', 'pdf', 'docx']:
        #     file_info.download('temp_file.' + file_extension)

        src = r"handlers/custom_handlers/" + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        engine = pyttsx3.init()

        vioces = engine.getProperty('voices')
        engine.setProperty('voice', 'ru')

        for vioce in vioces:
            if vioce.name == 'Alena':
                engine.setProperty('voice', vioce.id)

        with open(src, 'r', encoding='utf-8') as f:
            text = f.read()
        print(text)

        engine.save_to_file(text,
                            r"handlers/custom_handlers/output.wav")
        engine.runAndWait()

        # Отправляем голосовой ответ пользователю
        with open(r"handlers/custom_handlers/output.wav", 'rb') as f:
            bot.send_voice(message.chat.id, voice=f.read())

    except Exception as e:
        bot.reply_to(message, e)
