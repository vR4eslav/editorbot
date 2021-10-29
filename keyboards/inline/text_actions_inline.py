from aiogram import types
from loader import _


async def text_actions_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=_('📝 Посчитать символы 📝'), callback_data='count_symbols')
    btn2 = types.InlineKeyboardButton(text=_('📠 Посчитать слова 📠'), callback_data='count_words')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton(text=_('🔍 Проверить грамотность 🔍'), callback_data='check_spelling')
    btn4 = types.InlineKeyboardButton(text=_('🔁 Поменять регистр 🔁'), callback_data='change_register')
    markup.row(btn3, btn4)
    btn5 = types.InlineKeyboardButton(text=_('🔑 Сгенерировать надежный пароль 🔑'), callback_data='generate_password')
    markup.add(btn5)
    # btn6 = types.InlineKeyboardButton(text='✒️ Сделать рукописный текст ✒️', callback_data='text_to_hand')
    # text_actions_keyboard.add(btn6)
    btn7 = types.InlineKeyboardButton(text=_('🔥 ПЕРЕВЕСТИ ФОТО В ТЕКСТ(BETA) 🔥'), callback_data='photo_to_text')
    markup.add(btn7)
    btn9 = types.InlineKeyboardButton(text=_('🔙 НАЗАД В МЕНЮ 🔙'), callback_data='back_to_menu')
    markup.add(btn9)
    return markup
