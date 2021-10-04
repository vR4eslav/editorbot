from aiogram import types

admin_panel = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text='Узнать количество пользователей', callback_data='count_users')
admin_panel.row(btn1)
