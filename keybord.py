from telebot import types

markup_zypunka_close = types.InlineKeyboardMarkup(row_width=1)
item_zypunka = types.InlineKeyboardButton('Вибрати інший час', callback_data='Вибрати інший час')
markup_zypunka_close.add(item_zypunka)

markup_KNB_close = types.InlineKeyboardMarkup(row_width=1)
item_KNB = types.InlineKeyboardButton('Зіграймо ще раз!', callback_data='Зіграймо ще раз!')
markup_KNB_close.add(item_KNB)

markup_KNB__close = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
item1 = types.KeyboardButton('Зіграймо ще раз!')
markup_KNB__close.add(item1)

markup_porahuy = types.InlineKeyboardMarkup(row_width=2) # test
item1 = types.InlineKeyboardButton('Додавання', callback_data='Додавання')
item2 = types.InlineKeyboardButton('Віднімання', callback_data='Віднімання')
item3 = types.InlineKeyboardButton('Множення', callback_data='Множення')
item4 = types.InlineKeyboardButton('Ділення', callback_data='Ділення')
markup_porahuy.add(item1, item2, item3, item4)

markup_zypunka = types.InlineKeyboardMarkup(row_width=1) # клавіатура зупинок
item1 = types.InlineKeyboardButton('Скотофуражний ринок', callback_data='Скотофуражний ринок')
item2 = types.InlineKeyboardButton('Центр-->Цукровий завод', callback_data='Центр-->Цукровий завод')
item3 = types.InlineKeyboardButton('Цукровий завод', callback_data='Цукровий завод')
item4 = types.InlineKeyboardButton('Центр-->Військове містечко', callback_data='Центр-->Військове містечко')
item5 = types.InlineKeyboardButton('АТП «Вантажне»', callback_data='АТП «Вантажне»')
item6 = types.InlineKeyboardButton('вул. Степана Бандери', callback_data='вул. Степана Бандери')
item7 = types.InlineKeyboardButton('вул.П.Січі', callback_data='вул.П.Січі')
item8 = types.InlineKeyboardButton('вул. Зимнівська', callback_data='вул. Зимнівська')
markup_zypunka.add(item1, item2, item3, item4, item5, item6, item7, item8)

# markup_close = types.ReplyKeyboardRemove(selective=False) # закриває клавіатуру

markup_time = types.InlineKeyboardMarkup(row_width=2) # вибір часу зупинки
item1 = types.InlineKeyboardButton('07:00-08:00', callback_data='07:00-08:00')
item2 = types.InlineKeyboardButton('08:00-09:00', callback_data='08:00-09:00')
item3 = types.InlineKeyboardButton('09:00-10:00', callback_data='09:00-10:00')
item4 = types.InlineKeyboardButton('10:00-11:00', callback_data='10:00-11:00')
item5 = types.InlineKeyboardButton('11:00-12:00', callback_data='11:00-12:00')
item6 = types.InlineKeyboardButton('12:00-13:00', callback_data='12:00-13:00')
item7 = types.InlineKeyboardButton('13:00-14:00', callback_data='13:00-14:00')
item8 = types.InlineKeyboardButton('14:00-15:00', callback_data='14:00-15:00')
item9 = types.InlineKeyboardButton('15:00-16:00', callback_data='15:00-16:00')
item10 = types.InlineKeyboardButton('16:00-17:00', callback_data='16:00-17:00')
item11 = types.InlineKeyboardButton('17:00-18:00', callback_data='17:00-18:00')
item12 = types.InlineKeyboardButton('18:00-19:00', callback_data='18:00-19:00')
item13 = types.InlineKeyboardButton('19:00-20:00', callback_data='19:00-20:00')
item14 = types.InlineKeyboardButton('20:00-21:00', callback_data='20:00-21:00')
markup_time.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14)

markup_KNB = types.InlineKeyboardMarkup(row_width=4) # Клавіатура гри Камінь Ножиці Бумага
item1 = types.InlineKeyboardButton('🪨', callback_data='stone')
item2 = types.InlineKeyboardButton('✂', callback_data='scissors')
item3 = types.InlineKeyboardButton('📄', callback_data='paper')
markup_KNB.add(item1, item2, item3)