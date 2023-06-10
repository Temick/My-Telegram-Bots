'''Примеры простых Инлайн-Ботов'''
import uuid
import hashlib
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

from config import TOKKEN

bot = Bot(token=TOKKEN)
dp = Dispatcher(bot=bot)


# Простой Инлайн-Бот который даёт несколько вариантов ответа
'''
async def on_startup(_):
    print('Work!')

@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    text = inline_query.query or "Empty"
    input_b_content = InputTextMessageContent(message_text=f'<b>{text}</b>',
                                            parse_mode='HTML')
    input_it_content = InputTextMessageContent(message_text=f'<em>{text}</em>',
                                            parse_mode='HTML')

    item_b = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_b_content,
        title='Bold',
        description='Empty',
        thumb_url='https://d144mzi0q5mijx.cloudfront.net/img/T/H/The-Bold-Font.png'
    )
    item_it = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_it_content,
        title='Italic',
        description='Empty',
        thumb_url='http://legionfonts.com/img-fonts/arial-italic/arial-italic-font.jpg'
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item_b,item_it],
                                  cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)'''
                           
# Простой Инлайн-Бот который запоминает результат и выводит вам Его
'''
user_number = ''

async def on_startup(_):
    print('Work!')

@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await message.answer(text='Введите ваше число!')
    
@dp.message_handler()
async def text_comand(message: types.Message):
    global user_number
    user_number = message.text
    await message.reply(text='Ваше число сохранено')

@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    text = inline_query.query or "Echo"
    result_id = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f'<b>{text}</b> - {user_number}',
                                            parse_mode='HTML')
    
    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Echo Bot!',
        description='Привет, я не простой ЭХО Бот'
    )

    await bot.answer_inline_query(results=[item],
                                  inline_query_id=inline_query.id,
                                  cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)'''

# Простой Эхо_Инлайн_Бот
'''
cb = CallbackData('ikb','action')

def get_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Button 1', callback_data=cb.new('push_1'))],
        [InlineKeyboardButton('Button 2', callback_data=cb.new('push_2'))]
    ])
    return ikb

async def on_startup(_):
    print('Work!')

@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome to my InlineBot',
                           reply_markup=get_ikb())

@dp.callback_query_handler(cb.filter(action='push_1'))
async def push1_handler(callback: types.CallbackQuery):
    await callback.answer('Hello!')

@dp.callback_query_handler(cb.filter(action='push_2'))
async def push2_handler(callback: types.CallbackQuery):
    await callback.answer('Word!')

@dp.inline_handler()
async def inline_command(inline_query: types.InlineQuery):
    text = inline_query.query or "Echo"
    if 'photo' in text:
        input_content = InputTextMessageContent('This is photo')
    else:
        input_content = InputTextMessageContent(text)
    result_id = hashlib.md5(text.encode()).hexdigest()

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Echo'
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)'''