from telebot import types
import random

def plys(x, y):
    value = x + y
    r50 = random.randint(0, 50) # цифри на кнопках підсказках
    r20 = random.randint(0, 20) # цифри на кнопках підсказках
    r10 = random.randint(0, 10) # цифри на кнопках підсказках
    markup = types.InlineKeyboardMarkup(row_width=2, )
    item1 = types.InlineKeyboardButton(value, callback_data='value')
    if r20 != value:
        item2 = types.InlineKeyboardButton(r20, callback_data='arror1')
    else:
        r20 = + 1
        item2 = types.InlineKeyboardButton(r20, callback_data='arror1')
    if r10 != value:
        item3 = types.InlineKeyboardButton(r10, callback_data='arror2')
    else:
        r10 = + 1
        item3 = types.InlineKeyboardButton(r10, callback_data='arror2')
    if r50 != value:
        item4 = types.InlineKeyboardButton(r50, callback_data='arror3')
    else:
        r50 = + 1
        item4 = types.InlineKeyboardButton(r50, callback_data='arror3')

    x = [item1, item2, item3, item4]  # рамдомно перемішує кнопки під повідомленням
    random.shuffle(x)
    markup.add(x[0], x[1], x[2], x[3])
    return markup

def minus(x, y):
    value = x - y
    r50 = random.randint(0, 50) # цифри на кнопках підсказках
    r20 = random.randint(0, 20) # цифри на кнопках підсказках
    r10 = random.randint(0, 10) # цифри на кнопках підсказках
    markup = types.InlineKeyboardMarkup(row_width=2, )
    item1 = types.InlineKeyboardButton(value, callback_data='value')
    if r20 != value:
        item2 = types.InlineKeyboardButton(r20, callback_data='arror1')
    else:
        r20 = + 1
        item2 = types.InlineKeyboardButton(r20, callback_data='arror1')
    if r10 != value:
        item3 = types.InlineKeyboardButton(r10, callback_data='arror2')
    else:
        r10 = + 1
        item3 = types.InlineKeyboardButton(r10, callback_data='arror2')
    if r50 != value:
        item4 = types.InlineKeyboardButton(r50, callback_data='arror3')
    else:
        r50 = + 1
        item4 = types.InlineKeyboardButton(r50, callback_data='arror3')

    x = [item1, item2, item3, item4]  # рамдомно перемішує кнопки під повідомленням
    random.shuffle(x)
    markup.add(x[0], x[1], x[2], x[3])
    return markup

def multiplication(x, y):
    value = x * y
    r50 = random.randint(0, 50) # цифри на кнопках підсказках
    r20 = random.randint(10, 30) # цифри на кнопках підсказках
    r10 = random.randint(10, 20) # цифри на кнопках підсказках
    markup = types.InlineKeyboardMarkup(row_width=2, )
    item1 = types.InlineKeyboardButton(value, callback_data='value')
    if r20 != value:
        item2 = types.InlineKeyboardButton(r20, callback_data='arror1')
    else:
        r20 = + 1
        item2 = types.InlineKeyboardButton(r20, callback_data='arror1')
    if r10 != value:
        item3 = types.InlineKeyboardButton(r10, callback_data='arror2')
    else:
        r10 = + 1
        item3 = types.InlineKeyboardButton(r10, callback_data='arror2')
    if r50 != value:
        item4 = types.InlineKeyboardButton(r50, callback_data='arror3')
    else:
        r50 = + 1
        item4 = types.InlineKeyboardButton(r50, callback_data='arror3')

    x = [item1, item2, item3, item4]  # рамдомно перемішує кнопки під повідомленням
    random.shuffle(x)
    markup.add(x[0], x[1], x[2], x[3])
    return markup

def division(x, y):
    value = int(x / y)
    r50 = random.randint(0, 50) # цифри на кнопках підсказках
    r20 = random.randint(0, 20) # цифри на кнопках підсказках
    r10 = random.randint(0, 10) # цифри на кнопках підсказках
    markup = types.InlineKeyboardMarkup(row_width=2, )
    item1 = types.InlineKeyboardButton(value, callback_data='value')
    if r20 != value:
        item2 = types.InlineKeyboardButton(r20, callback_data='arror1')
    else:
        r20 = + 1
        item2 = types.InlineKeyboardButton(r20, callback_data='arror1')
    if r10 != value:
        item3 = types.InlineKeyboardButton(r10, callback_data='arror2')
    else:
        r10 = + 1
        item3 = types.InlineKeyboardButton(r10, callback_data='arror2')
    if r50 != value:
        item4 = types.InlineKeyboardButton(r50, callback_data='arror3')
    else:
        r50 = + 1
        item4 = types.InlineKeyboardButton(r50, callback_data='arror3')

    x = [item1, item2, item3, item4]  # рамдомно перемішує кнопки під повідомленням
    random.shuffle(x)
    markup.add(x[0], x[1], x[2], x[3])
    return markup
