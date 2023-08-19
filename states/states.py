from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    enter_text = State()