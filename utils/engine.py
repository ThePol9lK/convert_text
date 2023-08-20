import pyttsx3


class Engine:
    PATH_AUDIO = 'utils/save_audio/output.mp3'

    def __init__(self):
        self.engine = pyttsx3.init()

    def set_property(self):
        self.engine.setProperty('volume', 0.8)
        self.engine.setProperty("rate", 200)
        self.engine.setProperty('voice', 'ru')

    @classmethod
    def auidoi(cls, text):
        en = cls()
        en.engine.save_to_file(text, en.PATH_AUDIO)
        en.engine.runAndWait()
