from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup






# клавиатура для Randomбота
'''
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
b1 = KeyboardButton(text='/start')
b2 = KeyboardButton(text='/help')
b3 = KeyboardButton(text='/description')
b4 = KeyboardButton(text='/location')
b6 = KeyboardButton(text='/sticker')
b7 = KeyboardButton(text='/emoji')
b8 = KeyboardButton(text='Random photo')
kb.add(b1,b2,b3,b4,b6,b7,b8)

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
pb1 = KeyboardButton(text='Рандом')
pb2 = KeyboardButton(text='Главное меню')
kb_photo.add(pb1,pb2)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Сдедующее фото',
                           callback_data='next')
ib2 = InlineKeyboardButton(text='Лайк',
                           callback_data='like')
ib3 = InlineKeyboardButton(text='Дизлайк',
                           callback_data='dis')
ikb.add(ib1,ib2,ib3)'''