from aiogram import types
from loader import _

admin_panel = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text=_('Узнать количество пользователей'), callback_data='count_users')
admin_panel.row(btn1)
