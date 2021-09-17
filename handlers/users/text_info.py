from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.text_actions_inline import text_actions_keyboard
from loader import dp, bot
from states.text_info_states import TextInfo


@dp.message_handler(Command('menu'))
async def text_info_message_msg(message: types.Message):
    await message.answer('✏️ Что нужно узнать о тексте? ✏️',
                         reply_markup=text_actions_keyboard)


@dp.callback_query_handler(text='menu')
async def text_info_message_cq(call: CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                text=f'✏️ Что нужно узнать о тексте? ✏️',
                                reply_markup=text_actions_keyboard)
