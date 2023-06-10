from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler

from config import TOKKEN

bot = Bot(token=TOKKEN)
dp = Dispatcher(bot=bot)

ADMIN = 'user_id'

# простой бот с Middleware с ограничением к функциям для разных пользователей
'''
class CheckMiddleware(BaseMiddleware):
	
	async def on_process_callback_query(self, callback: types.CallbackQuery, data: dict):

		callback_id = callback.data[callback.data.find('_')+1:]

		if callback_id != str(callback.from_user.id):
			print('NO')
			raise CancelHandler()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
	ikb = types.InlineKeyboardMarkup(inline_keyboard=[
					 [types.InlineKeyboardButton('Тестовая кнопка',callback_data=f'check_{message.from_user.id}')]])
	await message.reply('Ты написал команду старт', reply_markup=ikb)

@dp.callback_query_handler(lambda callback: callback.data.startswith('check_'))
async def cmd_callback(callback: types.CallbackQuery):
	await callback.answer('Тестовое сообщение')

if __name__ == '__main__':
	dp.middleware.setup(CheckMiddleware())
	executor.start_polling(dp,skip_updates=True)'''


# простой пример с Middleware с декоратором
'''
def set_key(key: str = None):

	def decorator(func):
		setattr(func, 'key', key)
	
		return func

	return decorator

class AdminMiddleware(BaseMiddleware):
	
	async def on_process_message(self, message: types.Message, data: dict):

		handler = current_handler.get()

		if handler:
			key = getattr(handler, 'key', 'Такого атрибута нет')
			print(key)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
	await message.reply('Ты написал команду старт')

@dp.message_handler(lambda message: message.text.lower() == 'привет')
@set_key('hello!')
async def hi(message: types.Message):
	await message.answer('ты написал привет')


if __name__ == '__main__':
	dp.middleware.setup(AdminMiddleware())
	executor.start_polling(dp,skip_updates=True)
'''

# простой пример бота с Middleware с ограничением права доступа
'''
class CustomMiddleware(BaseMiddleware):
	async def on_process_message(self, message: types.Message, data: dict):
		if message.from_user.id != ADMIN:
			print('НЕТ!')
			raise CancelHandler()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
	await message.reply('Ты написал команду старт')

@dp.message_handler(lambda message: message.text.lower() == 'привет')
async def hi(message: types.Message):
	await message.answer('ты написал привет')


if __name__ == '__main__':
	dp.middleware.setup(CustomMiddleware())
	executor.start_polling(dp,skip_updates=True)
'''


# простой пример работы с Middleware
'''
class TestMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update, data): print('Hello!')
    async def on_process_update(self, update, data):
	    print('dfsdfsv')

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
	await message.reply('Ты написал команду старт')

if __name__ == '__main__':
	dp.middleware.setup(TestMiddleware())
	executor.start_polling(dp,skip_updates=True)
'''