from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from asyncpg import UniqueViolationError

from keyboards.inline.text_actions_inline import text_actions_keyboard
from loader import dp, bot, db
from states.text_info_states import TextInfo


@dp.message_handler(Command('menu'))
async def text_info_message_msg(message: types.Message):
    try:
        await db.add_user(full_name=message.from_user.full_name,
                          username=message.from_user.username,
                          telegram_id=message.from_user.id)
    except UniqueViolationError:
        pass
    await message.answer('✏️ Что нужно узнать о тексте? ✏️',
                         reply_markup=text_actions_keyboard)


@dp.callback_query_handler(text='menu')
async def text_info_message_cq(call: CallbackQuery):
    try:
        await db.add_user(full_name=call.from_user.full_name,
                          username=call.from_user.username,
                          telegram_id=call.from_user.id)
    except UniqueViolationError:
        pass
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                text=f'✏️ Что нужно узнать о тексте? ✏️',
                                reply_markup=text_actions_keyboard)


@dp.callback_query_handler(text='back_to_menu_from_file')
async def text_info_message_cq(call: CallbackQuery):
    try:
        await db.add_user(full_name=call.from_user.full_name,
                          username=call.from_user.username,
                          telegram_id=call.from_user.id)
    except UniqueViolationError:
        pass
    await call.message.delete()
    await call.message.answer(text=f'✏️ Что нужно узнать о тексте? ✏️',
                              reply_markup=text_actions_keyboard)