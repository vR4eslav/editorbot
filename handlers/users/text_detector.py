import os

import cv2
import pytesseract

# Путь для подключения tesseract для виндовс
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, CallbackQuery

from keyboards.inline.cancel_keyboard_inline import keyboard_cancel
from keyboards.inline.text_actions_inline import text_actions_keyboard
from loader import dp, bot


# windows
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


async def text_downloader(message):
    user_id = message.from_user.id
    photo_path = f'data/temp_photo_to_text/{user_id}.jpg'
    await message.photo[-1].download(destination=photo_path)
    return photo_path


async def text_detector(photo):
    # Подключение фото
    img = cv2.imread(photo)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Будет выведен весь текст с картинки
    config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=config, lang='rus+eng')
    return text


@dp.callback_query_handler(text='photo_to_text')
async def start_converting(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        text='💾Отправьте мне фото, которое нужно конвертировать в текст! Нейросеть постарается это '
             'сделать\n'
             'Вы можете присылать код программы, рукописный текст, а также скриншоты текста с '
             'разных сайтов', reply_markup=keyboard_cancel)
    await state.set_state('image_convert')


@dp.message_handler(Command('photo_to_text'))
async def start_converting(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Отправьте мне фото, которое нужно конвертировать в текст! Нейросеть постарается это '
                                'сделать\n'
                                'Вы можете присылать код программы, рукописный текст, а также скриншоты текста с '
                                'разных сайтов', reply_markup=keyboard_cancel)
    await state.set_state('image_convert')


@dp.message_handler(state='image_convert', content_types=ContentType.ANY)
async def process_convert(message: types.Message, state: FSMContext):
    try:
        photo = await text_downloader(message=message)
        text = await text_detector(photo=photo)
        await message.edit_text(text=f'☑️ Ваш текст: \n\n'
                                     f'{text}\n\n'
                                     f'Что нужно сделать еще?', parse_mode="", reply_markup=text_actions_keyboard)
        os.remove(photo)
    except:
        await message.answer(text=f'📛Произошла неизвестная ошибка! Мы уже отправили очет разработчикам.\n\n'
                                  f'Попробуйте отправить фотографию <b>не документом</b>',
                             reply_markup=text_actions_keyboard)
    await state.reset_state()


@dp.callback_query_handler(text='cancel', state='image_convert')
async def cancel_convert(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text=f'❗️Вы отменили перевод текста в фото! Что вы хотите сделать еще?',
                                 reply_markup=text_actions_keyboard)
    await state.reset_state()
