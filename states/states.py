from telebot.handler_backends import State, StatesGroup


class UserDocument(StatesGroup):
    """
    Класс состояний для состояний обработки документов
    """
    enter_document = State()


class UserText(StatesGroup):
    """
    Класс состояний для состояний обработки текста
    """
    enter_text = State()
