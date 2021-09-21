import random

from aiogram.types import CallbackQuery

from keyboards.inline.text_actions_inline import text_actions_keyboard
from loader import dp, bot


async def password_gen(length):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '[]{}()*;/,_-'

    all = lower + upper + numbers + symbols
    password: str = ''.join(random.sample(all, length))
    return password


@dp.callback_query_handler(text='generate_password')
async def start_generating(call: CallbackQuery):
    password = await password_gen(17)
    await call.message.edit_text(text=f'☑️ Ваш пароль успешно сгенерирован!\n\n'
                                      f'<code>{password}</code>\n\n'
                                      f'Что нужно сделать еще?', reply_markup=text_actions_keyboard)


@dp.message_handler(text='/generate_password')
async def start_generating(message: CallbackQuery):
    password = await password_gen(17)
    await bot.send_message(chat_id=message.from_user.id, text=f'☑️ Ваш пароль успешно сгенерирован!\n\n'
                                                              f'<code>{password}</code>\n\n'
                                                              f'Что нужно сделать еще?',
                           reply_markup=text_actions_keyboard)
