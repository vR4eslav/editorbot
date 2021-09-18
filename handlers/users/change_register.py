from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.cancel_keyboard_inline import keyboard_cancel
from keyboards.inline.text_actions_inline import text_actions_keyboard
from loader import dp, bot
from states.change_register_states import ChangeRegister


# data = await state.get_data()
# answer1 = float(data.get('mass'))

async def start_changing(chat_id, message_id):
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                text=f"📝Отправь сообщение для смены регистра, не более <b>4096</b> символов! Если "
                                     f"символов больше, "
                                     f"разделите текст на несколько сообщений. ", reply_markup=keyboard_cancel)


@dp.message_handler(Command('change_register'))
async def change_register_start_message(message: types.Message):
    await start_changing(chat_id=message.from_user.id, message_id=message.message_id)
    await ChangeRegister.stage1.set()


@dp.callback_query_handler(text='change_register')
async def change_register_start_cq(call: CallbackQuery):
    await start_changing(chat_id=call.from_user.id, message_id=call.message.message_id)
    await ChangeRegister.stage1.set()


@dp.message_handler(state=ChangeRegister.stage1)
async def change_register_process1(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['text'] = message.text
    except:
        await message.answer('Возника какая-то ошибка! Вполне возможно, Ваше сообщение слишком большое!')
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='В верхний регистр', callback_data='need_upper')
    keyboard.add(btn1)
    btn2 = types.InlineKeyboardButton(text='В нижний регистр', callback_data='need_lower')
    keyboard.add(btn2)
    btn3 = types.InlineKeyboardButton(text='Сделать первые символы заглавными', callback_data='need_title')
    keyboard.add(btn3)
    await message.answer(f'В какой регистр нужно перевести сообщение?', reply_markup=keyboard)
    await ChangeRegister.stage2.set()


@dp.callback_query_handler(state=ChangeRegister.stage2)
async def change_register_final(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    answer1 = str(data.get('text'))
    if call.data == 'need_upper':
        result = answer1.upper()
        await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                    text=f'☑️ Ваш измененный текст: \n\n'
                                         f'<code>{result}</code>', reply_markup=text_actions_keyboard)
    if call.data == 'need_lower':
        result = answer1.lower()
        await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                    text=f'☑️ Ваш измененный текст: \n\n'
                                         f'<code>{result}</code>', reply_markup=text_actions_keyboard)
    if call.data == 'need_title':
        result = answer1.title()
        await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                    text=f'☑️ Ваш измененный текст: \n\n'
                                         f'<code>{result}</code>', reply_markup=text_actions_keyboard)
    await state.reset_state()


@dp.callback_query_handler(state=ChangeRegister.stage1, text='cancel')
async def cancer_register_change(call: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                text=f'❗️Вы отменили смену регистра! Что вы хотите сделать еще?',
                                reply_markup=text_actions_keyboard)
    await state.reset_state()


@dp.callback_query_handler(state=ChangeRegister.stage2, text='cancel')
async def cancer_register_change(call: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                text=f'❗️Вы отменили смену регистра! Что вы хотите сделать еще?',
                                reply_markup=text_actions_keyboard)
    await state.reset_state()
