import asyncio
import logging
from os import replace
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

# CAT_BIG_EYES = 'AgADAgADNqkxG3hu6Eov3mINslrI7jUWnA4ABAX7PAfFIfbONj0AAgI'
# KITTENS = [
#     'AgADAgADN6kxG3hu6EqJjqtjb2_dtnztAw4ABMPliaCdHTFDDxsCAAEC',
#     'AgADAgADNakxG3hu6Epaq9GtKVQcmEPqAw4ABKKK02zsSoEJtRwCAAEC',
#     'AgADAgADNKkxG3hu6EoNC-hZek5IUkeZQw4ABPbUDtX7JTIZmjwAAgI',
# ]
# VOICE = 'AwADAgADXQEAAnhu6EqAvqdylJRvBgI'

# from config import TOKEN      
bot = Bot(token='5023919804:AAEbEZ5O_VqpXitmG8o1GA-ZNYTSG9Om3D4')
dp = Dispatcher(bot)


#Initilazing buttons
button_start = KeyboardButton("Start")
button_stt = KeyboardButton("Speech to text 💬")
# button_tts = KeyboardButton("Text to speech 📝")
button_resume = KeyboardButton("Resume builder 🗏")
markup2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_stt).add(button_resume)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Hello!\nuse /help, '
                        'to get instruction on using bot!', reply_markup=markup2)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Speech to text 💬":
        await bot.send_message(message.from_user.id, "Please send a voice, I will convert your voice into text")
    #if message.text == "Text to speech 📝":
    #    await bot.send_message(message.from_user.id, "Please send text, I will convert your text into voice")
    if message.text == "Resume builder 🗏":
        await bot.send_message(message.from_user.id, "Please provide enough materials to build your resume")
    


# @dp.callback_query_handler(lambda c: c.data == 'Resume builder 🗏')
# async def process_callback_button1(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(callback_query.from_user.id, 'Do you want to build your resume!')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = ('Too lazy to type? Then send your voice and let me type the te   xt for you!')
    await message.reply(msg)


@dp.message_handler(commands=['voice'])
async def process_voice_command(message: types.Message):
    await bot.send_voice(message.from_user.id, VOICE,
                            reply_to_message_id=message.message_id)



@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def photo_handler(message: types.Message):
    logging.info(message.voice)
    await message.answer("Bu bot hakaton davomida 2 kun ichida ishlab chiqilgan")




# @dp.message_handler(commands=['file'])
# async def process_file_command(message: types.Message):
#     user_id = message.from_user.id
#     await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
#     await asyncio.sleep(1)  # скачиваем файл и отправляем его пользователю
#     await bot.send_document(user_id, TEXT_FILE,
#                             caption='Этот файл специально для тебя!')


@dp.message_handler()
async def echo_message(msg: types.Message):
    logging.info(msg.text)
    await bot.send_message(msg.from_user.id, msg.text)


# @dp.message_handler(content_types=ContentType.ANY)
# async def unknown_message(msg: types.Message):
#     message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
#                         italic('\nЯ просто напомню,'), 'что есть',
#                         code('команда'), '/help')
#     await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)