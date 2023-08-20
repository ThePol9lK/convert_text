from telebot.handler_backends import State, StatesGroup


class UserDocument(StatesGroup):
    enter_document = State()

class UserText(StatesGroup):
    enter_text = State()