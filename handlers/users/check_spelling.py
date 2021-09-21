import re

import enchant
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageIsTooLong
from loguru import logger

from keyboards.inline.cancel_keyboard_inline import keyboard_cancel
from keyboards.inline.text_actions_inline import text_actions_keyboard
from loader import dp, bot
from states.check_text_states import CheckText

checker = enchant.Dict('ru_RU')


# b = c.check('верталет')
# b = c.suggest('ветролет')
# print(b)

async def text_checker(text_dict, normal_text, errors):
    text_dict = re.findall("[а-яё]+|[a-z]+", str(text_dict))
    for i in text_dict:
        checker_text = checker.check(i)
        if checker_text is True:
            normal_text.append(i)
        elif checker_text is False:
            errors.append(i)


async def start_check_func(chat_id, message_id):
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                text=f'📝Отправьте мне текст, который вы хотите проверить на ошибки'
                                     f'(не более <b>4096</b> символов!)\n\n'
                                     f'Пока что бот может проверить только текст на русском языке',
                                reply_markup=keyboard_cancel)


async def start_check_func_from_msg(chat_id):
    await bot.send_message(chat_id=chat_id,
                           text=f'📝Отправьте мне текст, который вы хотите проверить на ошибки'
                                f'(не более <b>4096</b> символов!)\n\n'
                                f'Пока что бот может проверить только текст на русском языке',
                           reply_markup=keyboard_cancel)


@dp.message_handler(Command('check_spelling'))
async def start_check(message: types.Message):
    await start_check_func_from_msg(chat_id=message.from_user.id)

    await CheckText.stage1.set()


@dp.callback_query_handler(text='check_spelling')
async def start_check(call: CallbackQuery):
    await start_check_func(chat_id=call.from_user.id, message_id=call.message.message_id)

    await CheckText.stage1.set()


@dp.message_handler(state=CheckText.stage1)
async def start_check(message: types.Message, state: FSMContext):
    text = message.text
    text_dict = []
    text_dict_dict = text.split()
    for i in text_dict_dict:
        text_dict.append(i.lower())
    logger.info(text_dict)
    normal_text = []
    errors = []
    try:
        await text_checker(text_dict=text_dict, normal_text=normal_text, errors=errors)
    except:
        await state.reset_state()
    try:
        if len(errors) > 0:
            errors = "\n".join(errors)
            await message.reply(f'⚠️<b>Ошибки: </b>⚠️ \n\n<code>{errors}</code> \n\nЧто нужно сделать еще?',
                                reply_markup=text_actions_keyboard)
        elif len(errors) <= 0:
            await message.reply(f'☑️Ошибок нет! Ура! \n\nЧто нужно сделать еще?',
                                reply_markup=text_actions_keyboard)
            await state.reset_state()
    except:
        await message.reply(f'🆘 Неизвестная ошибка!🆘 ', reply_markup=text_actions_keyboard)
        await state.reset_state()


@dp.callback_query_handler(state=CheckText.stage1, text='cancel')
async def cancel_check_spelling1(call: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                text=f'❗️Вы отменили проверку орфографии! Что вы хотите сделать еще?',
                                reply_markup=text_actions_keyboard)
    await state.reset_state()
