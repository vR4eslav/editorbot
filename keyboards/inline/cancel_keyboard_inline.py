from aiogram import types
from loader import _


async def keyboard_cancel():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=_('❌ Отмена ❌'), callback_data='cancel')
    markup.add(btn1)

    return markup
