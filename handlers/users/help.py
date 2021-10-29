from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from asyncpg import UniqueViolationError

from loader import dp, db, _
from utils.misc import rate_limit


@rate_limit(10, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton(text=_('🔙 НАЗАД В МЕНЮ 🔙'), callback_data='back_to_menu')
    keyboard.add(btn5)
    try:
        await db.add_user(full_name=message.from_user.full_name,
                          username=message.from_user.username,
                          telegram_id=message.from_user.id)
    except UniqueViolationError:
        pass
    await message.answer(_('📌 СПИСОК КОМАНД 📌\n\n'
                           '➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                           'Старт команды: \n\n'
                           '/start - Старт\n'
                           '/help - Помощь/Команды\n'
                           '/menu - Главное меню\n'
                           '/donate - Поддержать разработку\n'
                           '➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                           'Работа с текстом: \n\n'
                           '/change_register - Поменять регистр\n '
                           '/check_spelling - Проверить орфографию (поддерживается только 🇷🇺)\n'
                           '/count_words - Посчитать слова в тексте (поддержка 🇷🇺/🇬🇧)\n'
                           '/count_symbols - Посчитать количество символов в тексте (вместе с пробелами)\n'
                           '/generate_password - Сгенерировать пароль\n'
                           # f'/text_to_hand - Перевести текст в рукопись(поддерживается только 🇬🇧)\n'
                           '➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                           'Помощь: \n'
                           'Разработчик: botdevslava@gmail.com\n'
                           '➖➖➖➖➖➖➖➖➖➖➖➖➖\n'))
