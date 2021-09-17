from aiogram import types

keyboard_cancel = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text='❌ Отмена ❌', callback_data='cancel')
keyboard_cancel.add(btn1)