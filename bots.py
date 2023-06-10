'''Примеры простейших ботов'''

from aiogram import Bot, Dispatcher, executor,types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKKENBOTS
import string
import random

bot = Bot(TOKKENBOTS)
dp = Dispatcher(bot)


# бот с callback
'''
async def on_startup(_):
    print('Я запустился')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/vote')
kb.add(b1,b2)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome to our bot!',
                           reply_markup=kb)

@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=3)
    ib1 = InlineKeyboardButton(text='Yes',
                               callback_data='like')
    ib2 = InlineKeyboardButton(text="No",
                               callback_data='dislike')
    ikb.add(ib1,ib2)
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://krasivosti.pro/uploads/posts/2022-06/1655423871_61-krasivosti-pro-p-milie-malenkie-koshki-krasivo-foto-65.jpg",
                         caption='Тебе нравится данное фото?',
                         reply_markup=ikb)

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        return await callback.answer(text='Ура тебе понравилось!')
    await callback.answer(text='Жаль((((')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)'''


# бот с Инлайн клавиатурой
'''
async def on_startup(_):
    print('Я запустился')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/link')
kb.add(b1)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url='https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=11')
ib2 = InlineKeyboardButton(text='Button 2',
                           url='https://www.youtube.com/watch?v=AmT7P8b_cb8')
ikb.add(ib1,ib2)

@dp.message_handler(commands=['link'])
async def start_comand(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Случайные ссылки на ютюб',
                           reply_markup=ikb)

@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать',
                           reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)'''

# бот с клавиатурой

'''
async def on_startup(_):
    print('Я запустился')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')
b4 = KeyboardButton('❤️')
b5 = KeyboardButton('отправить апельсин')
b6 = KeyboardButton('/location')
kb.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6)

HELPCOMMAND = 
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание работы бота</em>
<b>/photo</b> - <em>отправка нашего фото</em>

@dp.message_handler(commands=['help'])
async def help_comand(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, 
                           text=HELPCOMMAND, 
                           parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, 
                           text='Добро пожаловать в наш бот!', 
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_comand(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, 
                           text='Наш бот умеет отправлять фото', parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['photo'])
async def send_img(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, 
                         photo="https://ae01.alicdn.com/kf/Hfef8b2bf5cb442cfb853b6ed6c75627bv.jpg")
    await message.delete()

@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id, 
                            latitude=70,
                            longitude=70)
    await message.delete()

@dp.message_handler()
async def send_kotik(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(chat_id=message.chat.id, 
                               sticker="CAACAgQAAxkBAAEJH5lkceVqRL87jDapibmiiNQ_bLVmDAACAQwAAuCHgVFGMXh8c_-m9C8E")
    if message.text == 'отправить апельсин':
        await bot.send_photo(chat_id=message.chat.id, 
                             photo="https://klike.net/uploads/posts/2022-12/1670819981_1.jpg")
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)'''

# бот для отправки фото и геолокации
'''
async def on_startup(_):
    print('Я запустился')

HELPCOMMAND = 
<b>/start</b> - <em>начало работы нашего бота</em>
<b>/help</b> - <em>список команд</em>
<b>/картинка</b> - <em>отправляет фото с котом</em>
<b>/location</b> - <em>отправляет локацию по коардинатам</em>


@dp.message_handler(commands=['help'])
async def help_comand(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELPCOMMAND, parse_mode='HTML')

@dp.message_handler(commands=['картинка'])
async def send_img(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://ae01.alicdn.com/kf/Hfef8b2bf5cb442cfb853b6ed6c75627bv.jpg")

@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=55, longitude=74)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)'''

# бот - эмодзи и их ID
'''
async def on_startup(_):
    print('Я запустился')

HELP_COMMAND =
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начало работы бота</em>
<b>/give</b> - <em>стикер с котом</em>

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='<em>Привет, <b>добро</b> пожаловать в наш бот</em>', parse_mode="HTML")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await message.answer('Смотри какой котик!❤️')
    await bot.send_sticker(message.from_user.id, sticker="CAACAgQAAxkBAAEJHjlkcQF_g0Skfo6DI_AFrXGu6iVEQQACxAcAAnCkiFF_smQ4-5ElIC8E")

@dp.message_handler()
async def send_emoji(message: types.Message):
    if message.text == '❤️':
        return await message.answer('🖤')
    await message.answer(f"{message.text + '❤️'}\nКоличество галочек: {message.text.count('✅')}")

@dp.message_handler(content_types=['sticker'])
async def send_stickers_id(message: types.Message):
    await message.answer(message.sticker.file_id)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)'''

# бот с рандомным символом алфавита

'''

COUNT = 0
HELP =
/start - начинаем работу с ботом
/help - список команд
/description - описание работы бота
/count - показывает количество собственных вызовов

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Привет, введите ваше сообщение")
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.reply(text='Данный бот в ответ на ваше сообщение показывает вам случайный символ алфавита, а также показывает YES, если сообщение содержит число 0 и NO в противном случае')

@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    global COUNT
    COUNT += 1
    await message.reply(text=COUNT)

@dp.message_handler()
async def random_symbol(message: types.Message):
    if '0' in message.text:
        await message.answer(text=f'{random.choice(string.ascii_letters)} YES')
    else:
        await message.answer(text=f'{random.choice(string.ascii_letters)} NO')

if __name__ == '__main__':
    executor.start_polling(dp)'''