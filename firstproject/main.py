from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked

from config import TOKKEN

import random
import asyncio

bot = Bot(token=TOKKEN)
dp = Dispatcher(bot=bot)

# бот пример работы с исключениями и ошибками
'''
async def on_startup(_):
    print('Work!')

@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await asyncio.sleep(10)
    await bot.send_message(chat_id=message.chat.id,
                           text='Hello')

@dp.errors_handler(exception=BotBlocked)
async def error_handler(update: types.Update, exeption: BotBlocked):
    print('Нельзя отправить сообщение бот заблокировали!')
    return True

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
'''

# бот с примером шаблона через класс CallbackData
'''
async def on_startup(_):
    print('Work!')

cb = CallbackData('ikb','action')

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Buton 1',callback_data=cb.new('push'))]
])

@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Text',
                           reply_markup=ikb)

@dp.callback_query_handler(cb.filter())
async def cb_command(callback: types.CallbackQuery, callback_data: dict):
    if callback_data['action'] == 'push':
        await callback.answer('something!')

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
'''

# бот выдающий рандомное число

'''
async def on_startup(_):
    print('Work!')

def get_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Random number',callback_data='random')]
    ])
    return ikb


@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Нажмите Random number, чтобы получить рандомное число',
                           reply_markup=get_ikb())

@dp.callback_query_handler()
async def random_cb_handler(callback: types.CallbackQuery):
    await callback.message.answer(text=f'Ваше рандомное число {random.randint(1,1000)}',
                                  reply_markup=get_ikb())

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)'''


# бот счётчик
'''
async def on_startup(_):
    print('Work!')

number = 0

def get_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Increase',callback_data='btn_increase'),
         InlineKeyboardButton('Decrease',callback_data='btn_decrease')],
        [InlineKeyboardButton('Random number',callback_data='btn_random')]
    ])
    return ikb

@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=f'The current number is {number}',
                           reply_markup=get_ikb())
    
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def ikb_cb_handler(callback: types.CallbackQuery):
    global number
    if callback.data == 'btn_increase':
        number += 1
        await callback.message.edit_text(f'The current number is {number}',
                                         reply_markup=get_ikb())
    elif callback.data == 'btn_decrease':
        number -= 1
        await callback.message.edit_text(f'The current number is {number}',
                                         reply_markup=get_ikb())
    else:
        number = random.randint(1,100)
        await callback.message.edit_text(f'The current number is {number}',
                                         reply_markup=get_ikb())

                                         
if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)'''



# бот с callback
'''
is_voted = True

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Нравится', callback_data='like'),
     InlineKeyboardButton('Не нравится', callback_data='dislike')],
    [InlineKeyboardButton('Close keyboard',callback_data='close')]
])

@dp.message_handler(commands=['start'])
async def cmd(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                           photo='https://img5.goodfon.ru/original/1920x1408/7/96/kotenok-malenkii-khvostik-fon.jpg',
                           caption="нравится ли тебе фото",
                           reply_markup=ikb)

@dp.callback_query_handler(text='close')
async def close_cb_handler(callback: types.CallbackQuery):
    await callback.message.delete()

@dp.callback_query_handler()
async def ikb_cb_handler(callback: types.CallbackQuery):
    global is_voted
    if is_voted:
        is_voted = False
        if callback.data == 'like':
            await callback.answer(text='Тебе понравилось фото')
        await callback.answer(text='Тебе не понравилось!')
    else:
        await callback.answer(text='Вы уже голосовали')

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)'''


# пример callback, он представляет из себя словарь с данными, при нажатии на Инлайн клавиатуру такой запрос обрабатывается callback_hendler
'''
{"id": "4876365958631556663", 
 "from": {"id": 1135367424, "is_bot": false, "first_name": "Артëм", "last_name": "Гарин", "username": "Artemkafunguy", "language_code": "ru"}, 
 "message": {"message_id": 274, 
             "from": {"id": 6013374440, "is_bot": true, "first_name": "project_bot", "username": "myFirstttt_bot"}, 
             "chat": {"id": 1135367424, "first_name": "Артëм", "last_name": "Гарин", "username": "Artemkafunguy", "type": "private"}, 
             "date": 1685282604, 
             "photo": [{"file_id": "AgACAgQAAxkDAAIBEmRzNPyb2Ukrx5qcJmKey0KappNJAALXrzEbUWSNUW0Ko_SiqxUqAQADAgADcwADLwQ", "file_unique_id": "AQAD168xG1FkjVF4", "file_size": 933, "width": 90, "height": 66}, 
                       {"file_id": "AgACAgQAAxkDAAIBEmRzNPyb2Ukrx5qcJmKey0KappNJAALXrzEbUWSNUW0Ko_SiqxUqAQADAgADbQADLwQ", "file_unique_id": "AQAD168xG1FkjVFy", "file_size": 11353, "width": 320, "height": 235}, 
                       {"file_id": "AgACAgQAAxkDAAIBEmRzNPyb2Ukrx5qcJmKey0KappNJAALXrzEbUWSNUW0Ko_SiqxUqAQADAgADeAADLwQ", "file_unique_id": "AQAD168xG1FkjVF9", "file_size": 59525, "width": 800, "height": 587}, 
                       {"file_id": "AgACAgQAAxkDAAIBEmRzNPyb2Ukrx5qcJmKey0KappNJAALXrzEbUWSNUW0Ko_SiqxUqAQADAgADeQADLwQ", "file_unique_id": "AQAD168xG1FkjVF-", "file_size": 156673, "width": 1280, "height": 939}, 
                       {"file_id": "AgACAgQAAxkDAAIBEmRzNPyb2Ukrx5qcJmKey0KappNJAALXrzEbUWSNUW0Ko_SiqxUqAQADAgADdwADLwQ", "file_unique_id": "AQAD168xG1FkjVF8", "file_size": 377120, "width": 1920, "height": 1408}], 
             "caption": "нравится ли тебе фото", 
             "reply_markup": {"inline_keyboard": [[{"text": "Нравится", "callback_data": "like"}, {"text": "Не нравится", "callback_data": "dislike"}]]}}, 
 "chat_instance": "5823090369155703264", 
 "data": "like"}'''

# Randomбот который может отправить вам стикер, рандомное фото и эмодзи
'''
from keyboards import kb,ikb,kb_photo
import random

bot = Bot(token=TOKKEN)
dp = Dispatcher(bot=bot)

HELP =
<b>/start</b> - <em>начало работы бота</em>
<b>/help</b> - <em>список команд</em>
<b>/description</b> - <em>описание работы бота</em>
<b>/location</b> - <em>случайная геопозиция</em>
<b>/stiker</b> - <em>стикер с котиком</em>
<b>/emoji</b> - <em>случайный эмодзи</em>
<b>Random foto</b> - <em>случайное фото</em>

PHOTO = [
    'https://mobimg.b-cdn.net/v3/fetch/2c/2c38ec7c72e3d0094f591d6f735a3b8e.jpeg',
    'https://img5.goodfon.ru/original/1920x1408/7/96/kotenok-malenkii-khvostik-fon.jpg',
    'https://mobimg.b-cdn.net/v3/fetch/ab/abe3205358479fa9e50955774a3c81f7.jpeg',
    'https://proprikol.ru/wp-content/uploads/2019/08/kartinki-nyashnye-kotiki-16.jpg',
    'https://krasivosti.pro/uploads/posts/2021-04/1617953205_37-p-koshki-malenkie-milie-40.jpg',
]

photos = dict(zip(PHOTO,['Котик','Красивый котик','Милый котик','Милаха','клёвый котик']))

async def on_startup(_):
    print('Work!')

@dp.message_handler(Text(equals='Random photo'))
async def randomphoto_comand(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Для того чтобы получить рандомную фотографию нажмите на кнопку "Рандом"',
                           reply_markup=kb_photo)

@dp.message_handler(Text(equals='Рандом'))
async def randphoto_comand(message: types.Message):
    random_photo = random.choice(PHOTO)
    await bot.send_photo(chat_id=message.chat.id,
                           photo=random_photo,
                           caption=photos[random_photo],
                           reply_markup=ikb)

@dp.message_handler(Text(equals='Главное меню'))
async def mainmenu_comand(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Добро пожаловать в главное меню',
                           reply_markup=kb)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome in my bot!',
                           reply_markup=kb)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP,
                           parse_mode='HTML')

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Этот бот может позволить вам поучавствовать в голосовании, или получить случайные координаты')

@dp.message_handler(commands=['location'])
async def location_command(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                           latitude=random.randrange(1,100),
                           longitude=random.randrange(1,100))

@dp.message_handler(commands=['sticker'])
async def stiker_command(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgQAAxkBAAEJIKBkcjjks8OMNOexouBJfrh7YJqKSwACWAgAAqLh6VMdo4c8L37lOC8E')
    
@dp.message_handler(commands=['emoji'])
async def emoji_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=random.choice('😐😅😂😱❤️🤔☹️😤😶😭💁‍♂️😏😩🙂😢😁😎'))

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.message.answer(text='Ура, тебе понравилось')
        await randphoto_comand(message=callback.message)
    elif callback.data == 'dis':
        await callback.message.answer(text='Жаль, вам не понравилось фото')
        await randphoto_comand(message=callback.message)
    else:
        await randphoto_comand(message=callback.message)
        await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)'''