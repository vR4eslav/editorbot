from aiogram import types

text_actions_keyboard = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text='📝 Посчитать символы 📝', callback_data='count_symbols')
btn2 = types.InlineKeyboardButton(text='📠 Посчитать слова 📠', callback_data='count_words')
text_actions_keyboard.row(btn1, btn2)
btn3 = types.InlineKeyboardButton(text='🔍 Проверить грамотность 🔍', callback_data='check_spelling')
btn4 = types.InlineKeyboardButton(text='🔁 Поменять регистр 🔁', callback_data='change_register')
text_actions_keyboard.row(btn3, btn4)
btn5 = types.InlineKeyboardButton(text='🔑 Сгенерировать надежный пароль 🔑', callback_data='generate_password')
text_actions_keyboard.add(btn5)
btn8 = types.InlineKeyboardButton(text='🔙 НАЗАД В МЕНЮ 🔙', callback_data='back_to_menu')
text_actions_keyboard.add(btn8)

