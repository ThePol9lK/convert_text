import os

import pyttsx3


class Engine:
    PATH_AUDIO = 'utils/'

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('volume', 0.8)
        self.engine.setProperty("rate", 200)
        self.engine.setProperty('voice', 'ru')

    # def set_property(self):
    #     self.engine.setProperty('volume', 0.8)
    #     self.engine.setProperty("rate", 200)
    #     self.engine.setProperty('voice', 'ru')

    def check_dir(self, user_name, file_name):
        if not os.path.exists(user_name):
            os.makedirs(f'{user_name}') # исправить ошибку
        right_path = f'utils/{user_name}/{file_name}.mp3'
        return right_path

    def create_audio(self, text, path):
        self.engine.save_to_file(text, path)
        self.engine.runAndWait()
