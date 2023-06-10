from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import re

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}, этот бот выдаёт гороскоп по твоей дате рождения. Введите дату рождения в формате <b>dd-mm-yyyy</b>',
                         parse_mode="HTML")

@dp.message_handler(content_types=['text'])
async def data_goroscop(message: types.Message):
    res = r'\d\d-\d\d-\d\d\d\d'
    if re.fullmatch(res, message.text):
        await message.answer('Чтобы узнать гороскоп нажми на кнопку <b>"Гороскоп"</b>',
                       parse_mode='HTML',
                       reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Гороскоп', web_app=WebAppInfo(url=f'https://moigoroskop.org/astroportret/{message.text}/'))))
    else:
        await message.answer('Неправильно введена дата, попробуйте ещё раз')


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)