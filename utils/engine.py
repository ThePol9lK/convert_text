import os
import pyttsx3


class Engine:
    """Класс для обработки mp3 файлов"""

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('volume', 0.8)
        self.engine.setProperty("rate", 200)
        self.engine.setProperty('voice', 'ru')

    def check_dir(self, user_name: str, file_name: str) -> str:
        """
        Метод где создается папка пользователя если ее нет и возвращает путь к этой папке
        :param user_name: str
        :param file_name: str
        :return right_path: str
        """
        if not os.path.exists(f'utils/{user_name}'):
            os.makedirs(f'utils/{user_name}')  # исправить ошибку
        right_path = f'utils/{user_name}/{file_name}.mp3'
        return right_path

    def create_audio(self, text: str, path: str):
        """
        Метод создания mp3 файла
        :param text: str
        :param path: str
        :return:
        """
        self.engine.save_to_file(text, path)
        self.engine.runAndWait()
