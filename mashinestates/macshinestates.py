from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

from config import TOKKEN
from sqlite import db_start,create_profile,edit_profile

async def on_startup(_):
	await db_start()
	print('Work!')

storage = MemoryStorage()
bot = Bot(token=TOKKEN)
dp=Dispatcher(bot=bot,
	      storage=storage)


# Простой бот с несколькими машинными состояниями, оформляющий профиль клиента
#'''
class ClientStateGroup(StatesGroup):
	photo = State()
	name = State()
	age = State()
	desc = State()

def get_keyboard():
	kb = ReplyKeyboardMarkup(resize_keyboard=True)
	kb.add(KeyboardButton('Начать работу!'))
	return kb

def get_cancel():
	return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
	await message.answer('Добро пожаловать', reply_markup=get_keyboard())
	await create_profile(user_id=message.from_user.id)

@dp.message_handler(commands=['cancel'], state='*')
async def cmd_start(message: types.Message, state: FSMContext):
	if state is None:
		return
	await message.reply('Отменил', reply_markup=get_keyboard())
	await state.finish()

@dp.message_handler(Text(equals='Начать работу!', ignore_case=True),state=None)
async def start_work(message: types.Message):
	await ClientStateGroup.photo.set()
	await message.answer('Сначала отправь фотографию', reply_markup=get_cancel())

@dp.message_handler(lambda message: not message.photo, state=ClientStateGroup.photo)
async def check_photo(message: types.Message):
	return await message.reply('Это не фотография!')

@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStateGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['photo'] = message.photo[0].file_id
	await ClientStateGroup.next()
	await message.reply('А теперь отправьте своё имя!')
	
@dp.message_handler(state=ClientStateGroup.name)
async def load_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await ClientStateGroup.next()
	await message.reply('А теперь отправьте ваш возраст')

@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) > 100, state=ClientStateGroup.age)
async def check_age(message: types.Message):
	await message.reply('Некоректный возраст')

@dp.message_handler(state=ClientStateGroup.age)
async def load_age(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['age'] = message.text
	await ClientStateGroup.next()
	await message.reply('А теперь отправьте ваше описание')

@dp.message_handler(state=ClientStateGroup.desc)
async def load_photo(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['desc'] = message.text
		await bot.send_photo(chat_id=message.from_user.id, photo=data['photo'], caption=f"{data['name']}, {data['age']}\n{data['desc']}")
	await edit_profile(state, user_id=message.from_user.id)
	await message.reply('Ваш профиль сохранен!')
	await state.finish()

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
#'''