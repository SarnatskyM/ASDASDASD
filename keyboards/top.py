from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


TopKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Топ 5"),
            KeyboardButton(text="Топ 30"),
        ],
        [
            KeyboardButton(text="Топ игроки"),
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True
)


Start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Результаты дня"),
            KeyboardButton(text="Топ"),
        ],
        [
            KeyboardButton(text="👀Помощь"),
        ]
    ],
    resize_keyboard=True
)