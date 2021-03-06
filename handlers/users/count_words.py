import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.cancel_keyboard_inline import keyboard_cancel
from keyboards.inline.text_actions_inline import text_actions_keyboard
from loader import bot, dp, _
from states.text_counter_states import Counter


async def start_counting(chat_id, message_id):
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                text=_('📝Отправьте текст, и я посчитаю, сколько в нем слов!\n\n'
                                       '<b>Не больше 4096 символов!</b>'),
                                reply_markup=await keyboard_cancel())


async def start_counting_from_msg(chat_id):
    await bot.send_message(chat_id=chat_id,
                           text=_('📝Отправьте текст, и я посчитаю, сколько в нем слов!\n\n'
                                  '<b>Не больше 4096 символов!</b>'),
                           reply_markup=await keyboard_cancel())


@dp.message_handler(Command('count_words'))
async def start_counting_message(message: types.Message):
    await start_counting_from_msg(chat_id=message.from_user.id)
    await Counter.stage1.set()


@dp.callback_query_handler(text='count_words')
async def start_counting_cq(call: CallbackQuery):
    await start_counting(chat_id=call.from_user.id, message_id=call.message.message_id)
    await Counter.stage1.set()


@dp.message_handler(state=Counter.stage1)
async def counting_process(message: types.Message, state: FSMContext):
    text = str(message.text)
    # text_list = text.split()
    # text_len = len(text_list)
    text_len = len(re.findall("[а-яё]+|[a-z]+", text))
    await bot.send_message(message.from_user.id, _('☑️Длина вашего текста: <b>{text_len}</b> слов!☑️ '
                                                   '\n\nЧто вы хотите сделать еще?').format(text_len=text_len),
                           reply_markup=await text_actions_keyboard())
    await state.reset_state()


@dp.callback_query_handler(state=Counter.stage1, text='cancel')
async def cancel_count(call: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                text=_('❗️Вы отменили подсчет символов! Что вы хотите сделать еще?'),
                                reply_markup=await text_actions_keyboard())
    await state.reset_state()
