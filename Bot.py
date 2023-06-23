import telebot
import Config
import random
import Pygoda
#import kyrs_valut
import marshrytku
import keybord
#import porahyu
from porahyu import plys, minus, multiplication, division
from telebot import types

bot = telebot.TeleBot(Config.TOKEN)
ad = 7 
@bot.message_handler(commands=['start'])
def welcome(message):
    if message.text == '/start':
        sti = open('1.png', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот створений тебе розважити!).".format(message.from_user, bot.get_me()), parse_mode='html') #, reply_markup=markup)

@bot.message_handler(commands=['kyrs'])
def kyrs(message):
    # bot.send_message(message.chat.id, f'Курс на сьогодні:\n {kyrs_valut.usd()}\n{kyrs_valut.euro()}\n  {kyrs_valut.pln()}\n\n{kyrs_valut.bitcoin()}\n{kyrs_valut.ethereum()}')
    bot.send_message(message.chat.id,'Сервіс тимчасово не працює!')

@bot.message_handler(commands=['pogoda'])
def pogoda(message):
    bot.send_message(message.chat.id, Pygoda.pogod)

    if Pygoda.temp <= 3:
        bot.send_message(message.chat.id, "🥶")
    if Pygoda.temp > 3 and Pygoda.temp <= 7:
        bot.send_message(message.chat.id, "🤧")
    if Pygoda.temp > 7 and Pygoda.temp <= 10:
        bot.send_message(message.chat.id, "😶‍🌫️")
    if Pygoda.temp > 10 and Pygoda.temp <= 14:
        bot.send_message(message.chat.id, "😄")
    if Pygoda.temp > 14 and Pygoda.temp <= 20:
        bot.send_message(message.chat.id, "😎")
    if Pygoda.temp > 20:
        bot.send_message(message.chat.id, "🥵")

        '''Гра Камінь, Ножиці, Бумага'''

@bot.message_handler(commands=['game'])
def welcome(game):

    bot.send_message(game.chat.id, "_______________ВИБИРАЙ_______________", reply_markup=keybord.markup_KNB)

    '''Порахуй'''

@bot.message_handler(commands=['porahyu'])
def welcome(message):
    if message.text == '/porahyu':
        bot.send_message(message.chat.id, "👇 Що робимо? 👇", reply_markup=keybord.markup_porahuy)

        '''PРозклад маршруток'''

@bot.message_handler(content_types =['text'])
def marshrytki(game):
    global ad

    if game.text == '/marshrytki':
        bot.send_message(game.chat.id, "⏱ Вибери години ⏱", parse_mode='html', reply_markup=keybord.markup_time)

#    if game.text == "Вимкнути клавіатуру":
 #       markup = types.ReplyKeyboardRemove(selective=True)
 #       bot.send_message(game.chat.id, 'Клавіатура вимкненна! Щоб знову її визвати впишіть /start', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global ad
    try:
        if call.message:
            # Для Кнопки матиматики
            if call.data == 'arror1':
                bot.send_message(chat_id=call.message.chat.id, text='Спробуй щераз!!!')
            if call.data == 'arror2':
                bot.send_message(chat_id=call.message.chat.id, text='Спробуй щераз!!!')
            if call.data == 'arror3':
                bot.send_message(chat_id=call.message.chat.id, text='Спробуй щераз!!!')
            if call.data == 'value':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👍", reply_markup=keybord.markup_porahuy)

            if call.data == 'Додавання':
                random_x = random.randint(1, 10)
                random_y = random.randint(1, 20)
                valueText = str(f'{random_x} + {random_y} =')
                bot.edit_message_text(
                    chat_id=call.message.chat.id, 
                    message_id=call.message.message_id, 
                    text=valueText, 
                    reply_markup=plys(random_x, random_y))
            
            if call.data == 'Віднімання':
                random_x = random.randint(1, 10)
                random_y = random.randint(10, 20)
                valueText = str(f'{random_y} - {random_x} =')
                bot.edit_message_text(
                    chat_id=call.message.chat.id, 
                    message_id=call.message.message_id, 
                    text=valueText, 
                    reply_markup=minus(random_y, random_x))
                
            if call.data == 'Множення':
                random_x = random.randint(1, 10)
                random_y = random.randint(1, 11)
                valueText = str(f'{random_x} x {random_y} =')
                bot.edit_message_text(
                    chat_id=call.message.chat.id, 
                    message_id=call.message.message_id, 
                    text=valueText, 
                    reply_markup=multiplication(random_x, random_y))
                
            if call.data == 'Ділення':
                random_x = random.randint(1, 10)
                random_y = random.randint(1, 11)
                divisionValue = random_x * random_y
                valueText = str(f'{divisionValue} / {random_x} =')
                bot.edit_message_text(
                    chat_id=call.message.chat.id, 
                    message_id=call.message.message_id,
                    text=valueText, 
                    reply_markup=division(divisionValue, random_x))

            # Для Кнопок гри В ЧУВУЧІ

            if call.data == 'stone':
                a = list('🪨✂📄')
                d = random.choice(a)
                bot.send_message(call.message.chat.id,'{0.first_name}'.format( call.message.from_user),parse_mode='html')
                bot.send_message(call.message.chat.id, '🪨')
                bot.send_message(call.message.chat.id, 'Бот:')
                bot.send_message(call.message.chat.id, d)
                if d == '🪨':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='нічия', reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id, text='__________Зіграймо ще раз!___________', reply_markup=keybord.markup_KNB)
                elif d == '✂':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ти виграв!😊', reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id, text='__________Зіграймо ще раз!___________', reply_markup=keybord.markup_KNB)
                elif d == '📄':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Бот виграв!😢', reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id, text='__________Зіграймо ще раз!___________', reply_markup=keybord.markup_KNB)

            elif call.data == 'scissors':
                a = list('🪨✂📄')
                d = random.choice(a)
                bot.send_message(call.message.chat.id, '{0.first_name}'.format(call.message.from_user), parse_mode='html')
                bot.send_message(call.message.chat.id, '✂')
                bot.send_message(call.message.chat.id, 'Бот:')
                bot.send_message(call.message.chat.id, d)
                if d == '✂':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='нічия', reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id, text='__________Зіграймо ще раз!___________', reply_markup=keybord.markup_KNB)
                elif d == '🪨':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Бот виграв!😢', reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id, text='__________Зіграймо ще раз!___________', reply_markup=keybord.markup_KNB)
                elif d == '📄':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ти виграв!😊', reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id, text='__________Зіграймо ще раз!___________', reply_markup=keybord.markup_KNB)

            elif call.data == 'paper':
                a = list('🪨✂📄')
                d = random.choice(a)
                bot.send_message(call.message.chat.id, '{0.first_name}'.format(call.message.from_user), parse_mode='html')
                bot.send_message(call.message.chat.id, '📄')
                bot.send_message(call.message.chat.id, 'Бот:')
                bot.send_message(call.message.chat.id, d)
                if d == '✂':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Бот виграв!😢', reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id, text='__________Зіграймо ще раз!___________', reply_markup=keybord.markup_KNB)
                elif d == '🪨':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ти виграв!😊', reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id, text='__________Зіграймо ще раз!___________', reply_markup=keybord.markup_KNB)
                elif d == '📄':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='нічия!', reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id, text='__________Зіграймо ще раз!___________', reply_markup=keybord.markup_KNB)

            # remove inline buttons

            if call.data == '07:00-08:00':
                ad = 7
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '08:00-09:00':
                ad = 8
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '09:00-10:00':
                ad = 9
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '10:00-11:00':
                ad = 10
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '11:00-12:00':
                ad = 11
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '12:00-13:00':
                ad = 12
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '13:00-14:00':
                ad = 13
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '14:00-15:00':
                ad = 14
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '15:00-16:00':
                ad = 15
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '16:00-17:00':
                ad = 16
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '17:00-18:00':
                ad = 17
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '18:00-19:00':
                ad = 18
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '19:00-20:00':
                ad = 19
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)
            if call.data == '20:00-21:00':
                ad = 20
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вибери зупинку 🚌", reply_markup=keybord.markup_zypunka)

            if call.data == 'Вибрати інший час':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⏱ Вибери години ⏱',
                                 reply_markup=keybord.markup_time)

            if call.data == 'Скотофуражний ринок' and ad:
                if marshrytku.warsity[str(ad)] != '':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=marshrytku.warsity[str(ad)],
                                 reply_markup=keybord.markup_zypunka_close)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Нажаль нічого не їздить 🤷‍♂️',
                                          reply_markup=keybord.markup_zypunka_close)
            if call.data == 'Центр-->Цукровий завод' and ad:
                if marshrytku.center_cyrovuy[str(ad)] != '':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=marshrytku.center_cyrovuy[str(ad)],
                                          reply_markup=keybord.markup_zypunka_close)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Нажаль нічого не їздить 🤷‍♂️',
                                          reply_markup=keybord.markup_zypunka_close)
            if call.data == 'Цукровий завод' and ad:
                if marshrytku.cykrovuy[str(ad)] != '':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=marshrytku.cykrovuy[str(ad)],
                                          reply_markup=keybord.markup_zypunka_close)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Нажаль нічого не їздить 🤷‍♂️',
                                          reply_markup=keybord.markup_zypunka_close)
            if call.data == 'Центр-->Військове містечко' and ad:
                if marshrytku.center[str(ad)] != '':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=marshrytku.center[str(ad)],
                                          reply_markup=keybord.markup_zypunka_close)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Нажаль нічого не їздить 🤷‍♂️',
                                          reply_markup=keybord.markup_zypunka_close)
            if call.data == 'АТП «Вантажне»' and ad:
                if marshrytku.atp[str(ad)] != '':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=marshrytku.atp[str(ad)],
                                          reply_markup=keybord.markup_zypunka_close)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Нажаль нічого не їздить 🤷‍♂️',
                                          reply_markup=keybord.markup_zypunka_close)
            if call.data == 'вул. Степана Бандери' and ad:
                if marshrytku.banderu[str(ad)] != '':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=marshrytku.banderu[str(ad)],
                                          reply_markup=keybord.markup_zypunka_close)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Нажаль нічого не їздить 🤷‍♂️',
                                          reply_markup=keybord.markup_zypunka_close)
            if call.data == 'вул.П.Січі' and ad:
                if marshrytku.sichi[str(ad)] != '':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=marshrytku.sichi[str(ad)],
                                          reply_markup=keybord.markup_zypunka_close)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Нажаль нічого не їздить 🤷‍♂️',
                                          reply_markup=keybord.markup_zypunka_close)
            if call.data == 'вул. Зимнівська' and ad:
                if marshrytku.zumnivska[str(ad)] != '':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=marshrytku.zumnivska[str(ad)],
                                          reply_markup=keybord.markup_zypunka_close)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Нажаль нічого не їздить 🤷‍♂️',
                                          reply_markup=keybord.markup_zypunka_close)
    except Exception as e:
        print(repr(e))

#Run Запуск

bot.polling(none_stop=True)
