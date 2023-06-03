import openai
import telebot
import Config
import random
import Pygoda
import kyrs_valut
import marshrytku
import keybord
from telebot import types

bot = telebot.TeleBot(Config.TOKEN)
openai.api_key = Config.key_openai
ad = 7
model_engine = 'text-davinci-003'

def generate_response(prompt):
    response = openai.Completion.create(engine=model_engine, prompt=prompt, presence_penalty=0, frequency_penalty=0, max_tokens=128, top_p=0.8, stop=[" Human:", " AI:"], temperature=0.8)
    message = response.choices[0].text
    return message

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.text.startswith('/start'):
        sti = open('1.png', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот створений тебе розважити!).".format(message.from_user, bot.get_me()), parse_mode='html')
        return
    if message.text.startswith('/kyrs'):
        bot.send_message(message.chat.id, f'Курс на сьогодні:\n\n{kyrs_valut.usd()}\n{kyrs_valut.euro()}\n{kyrs_valut.pln()}\n\n{kyrs_valut.bitcoin()}\n{kyrs_valut.ethereum()}')
        return
    if message.text.startswith('/pogoda'):
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
        return
    if message.text.startswith('/game'):
        bot.send_message(message.chat.id, "_______________ВИБИРАЙ_______________", reply_markup=keybord.markup_KNB)
        return
    if message.text.startswith('/marshrytki'):
        bot.send_message(message.chat.id, "⏱ Вибери години ⏱", parse_mode='html', reply_markup=keybord.markup_time)
        return
    if message.text.startswith('/porahyu'):
        t = random.randint(0, 20)  # співвідношення +(10%) -(10%) *(30%) /(50%)
        r = random.randint(2, 3)  # множення, ділення на 2 і 3
        a = random.randint(0, 20)
        b = random.randint(2, 10)
        c = random.randint(10, 20)
        c1 = random.randint(0, 50)  # цифри на кнопках підсказках
        a1 = random.randint(0, 20)  # цифри на кнопках підсказках
        b1 = random.randint(0, 10)  # цифри на кнопках підсказках
        if t == 0:
            w = a + b
            bot.send_message(message.chat.id, str(a) + '+' + str(b) + "=")

            markup = types.InlineKeyboardMarkup(row_width=2, )
            item1 = types.InlineKeyboardButton(w, callback_data='w')
            if a1 != w:
                item2 = types.InlineKeyboardButton(a1, callback_data='a')
            else:
                a1 = + 1
                item2 = types.InlineKeyboardButton(a1, callback_data='a')
            if b1 != w:
                item3 = types.InlineKeyboardButton(b1, callback_data='b')
            else:
                b1 = + 1
                item3 = types.InlineKeyboardButton(b1, callback_data='b')
            if c1 != w:
                item4 = types.InlineKeyboardButton(c1, callback_data='q')
            else:
                c1 = + 1
                item4 = types.InlineKeyboardButton(c1, callback_data='q')

            x = [item1, item2, item3, item4]  # рамдомно перемішує кнопки під повідомленням
            random.shuffle(x)

            markup.add(x[0], x[1], x[2], x[3])
            bot.send_message(message.chat.id, "👇 Вибери правильну відповідь 👇", reply_markup=markup)
        if t == 1:
            w = c - b
            bot.send_message(message.chat.id, str(c) + '-' + str(b) + "=")

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton(w, callback_data='w')
            if a1 != w:
                item2 = types.InlineKeyboardButton(a1, callback_data='a')
            else:
                a1 = + 1
                item2 = types.InlineKeyboardButton(a1, callback_data='a')
            if b1 != w:
                item3 = types.InlineKeyboardButton(b1, callback_data='b')
            else:
                b1 = + 1
                item3 = types.InlineKeyboardButton(b1, callback_data='b')
            if c1 != w:
                item4 = types.InlineKeyboardButton(c1, callback_data='q')
            else:
                c1 = + 1
                item4 = types.InlineKeyboardButton(c1, callback_data='q')

            x = [item1, item2, item3, item4]
            random.shuffle(x)

            markup.add(x[0], x[1], x[2], x[3])
            bot.send_message(message.chat.id, "👇 Вибери правильну відповідь 👇", reply_markup=markup)

        if t >= 2 and t <= 10:
            w = r * b
            bot.send_message(message.chat.id, str(r) + '*' + str(b) + "=")

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton(w, callback_data='w')
            if a1 != w:
                item2 = types.InlineKeyboardButton(a1, callback_data='a')
            else:
                a1 = + 1
                item2 = types.InlineKeyboardButton(a1, callback_data='a')
            if b1 != w:
                item3 = types.InlineKeyboardButton(b1, callback_data='b')
            else:
                b1 = + 1
                item3 = types.InlineKeyboardButton(b1, callback_data='b')
            if c1 != w:
                item4 = types.InlineKeyboardButton(c1, callback_data='q')
            else:
                c1 = + 1
                item4 = types.InlineKeyboardButton(c1, callback_data='q')

            x = [item1, item2, item3, item4]
            random.shuffle(x)

            markup.add(x[0], x[1], x[2], x[3])
            bot.send_message(message.chat.id, "👇 Вибери правильну відповідь 👇", reply_markup=markup)

        if t > 10 and t <= 20:
            d = r * b
            w = d / r
            bot.send_message(message.chat.id, str(d) + '/' + str(r) + "=")

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton(int(w), callback_data='w')
            if a1 != w:
                item2 = types.InlineKeyboardButton(a1, callback_data='a')
            else:
                a1 = + 1
                item2 = types.InlineKeyboardButton(a1, callback_data='a')
            if b1 != w:
                item3 = types.InlineKeyboardButton(b1, callback_data='b')
            else:
                b1 = + 1
                item3 = types.InlineKeyboardButton(b1, callback_data='b')
            if c1 != w:
                item4 = types.InlineKeyboardButton(c1, callback_data='q')
            else:
                c1 = + 1
                item4 = types.InlineKeyboardButton(c1, callback_data='q')

            x = [item1, item2, item3, item4]
            random.shuffle(x)

            markup.add(x[0], x[1], x[2], x[3])
            bot.send_message(message.chat.id, "👇 Вибери правильну відповідь 👇", reply_markup=markup)
        return
    response = generate_response(message.text)
    bot.send_message(message.chat.id, response)

#    if game.text == "Вимкнути клавіатуру":
 #       markup = types.ReplyKeyboardRemove(selective=True)
 #       bot.send_message(game.chat.id, 'Клавіатура вимкненна! Щоб знову її визвати впишіть /start', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global ad
    try:
        if call.message:
            # Для Кнопки матиматики
            if call.data == 'a':
                bot.send_message(chat_id=call.message.chat.id, text='Спробуй щераз!!!')
            if call.data == 'b':
                bot.send_message(chat_id=call.message.chat.id, text='Спробуй щераз!!!')
            if call.data == 'q':
                bot.send_message(chat_id=call.message.chat.id, text='Спробуй щераз!!!')
            if call.data == 'w':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👍")

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
