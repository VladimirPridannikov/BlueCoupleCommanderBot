#!/usr/bin/python3
# -*- coding: utf-8 -*-
import telebot
import sqlite3
from telebot import types

admin_list = [391545947, 64000151, 121485043, 339824315]
token = ''
bot = telebot.TeleBot(token)
CWBotID = 326394943


@bot.inline_handler(lambda query: query.query == 'Защита')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Защита', types.InputTextMessageContent('🛡 Защита'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query == '⚫️ Чёрный')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', '⚫️ Чёрный', types.InputTextMessageContent('⚫️ Чёрный'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query == '⚪️ Белый')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', '⚪️ Белый', types.InputTextMessageContent('⚪️ Белый'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query == 'Красный')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Красный', types.InputTextMessageContent('🔴 Красный'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query == '🌕 Жёлтый')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', '🌕 Жёлтый', types.InputTextMessageContent('🌕 Жёлтый'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query == '💥 Атака')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', '💥 Атака', types.InputTextMessageContent('💥 Атака'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.message_handler(commands=['red', 'blue', 'black', 'yellow', 'white', 'get_ready'])
def commands(message):
    send = 0
    bot.delete_message(message.chat.id, message.message_id)
    if '/red' in message.text and message.from_user.id in admin_list:
        blue = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Красный", switch_inline_query='Красный')
        blue.add(url_button)
        send = bot.send_message(message.chat.id, 'Итак сейчас самое время приготовиться к атаке на 🔴 Красный '
                                                 'квартал, для этого жмем на кнопку ниже, а потом на чат с игровым '
                                                 'ботом. Спасибо за внимание.', reply_markup=blue)
    elif '/blue' in message.text and message.from_user.id in admin_list:
        blue = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Защита", switch_inline_query='Защита')
        blue.add(url_button)
        send = bot.send_message(message.chat.id, 'Итак сейчас самое время приготовиться к защите 💙 Синего'
                                                 'квартала, для этого жмем на кнопку ниже, а потом на чат с игровым '
                                                 'ботом. Спасибо за внимание.', reply_markup=blue)
    elif '/black' in message.text and message.from_user.id in admin_list:
        blue = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="⚫️ Чёрный", switch_inline_query='⚫️ Чёрный')
        blue.add(url_button)
        send = bot.send_message(message.chat.id, 'Итак сейчас самое время приготовиться к атаке на ⚫️ Чёрный '
                                                 'квартал, для этого жмем на кнопку ниже, а потом на чат с игровым '
                                                 'ботом. Спасибо за внимание.', reply_markup=blue)
    elif '/yellow' in message.text and message.from_user.id in admin_list:
        blue = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="🌕 Жёлтый", switch_inline_query='🌕 Жёлтый')
        blue.add(url_button)
        send = bot.send_message(message.chat.id, 'Итак сейчас самое время приготовиться к атаке на 🌕 Жёлтый '
                                                 'квартал, для этого жмем на кнопку ниже, а потом на чат с игровым '
                                                 'ботом. Спасибо за внимание.', reply_markup=blue)
    elif '/white' in message.text and message.from_user.id in admin_list:
        blue = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="⚪️ Белый", switch_inline_query='⚪️ Белый')
        blue.add(url_button)
        send = bot.send_message(message.chat.id, 'Итак сейчас самое время приготовиться к атаке на ⚪️ Белый '
                                                 'квартал, для этого жмем на кнопку ниже, а потом на чат с игровым '
                                                 'ботом. Спасибо за внимание.', reply_markup=blue)
    elif 'get_ready' in message.text and message.from_user.id in admin_list:
        blue = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="💥 Атака", switch_inline_query='💥 Атака')
        blue.add(url_button)
        send = bot.send_message(message.chat.id, 'Итак, скоро битва, парни, поэтому прошу прямо сейчас ВСЕХ нажать на '
                                                 'кнопку ниже и переслать сообщение игровому боту, там выбрать в '
                                                 'выпадающем меню "💥 Атака" и некуда не уходить. Приказ на атаку/защиту'
                                                 ' будет через несколько минут. Спасибо.', reply_markup=blue)
    bot.pin_chat_message(message.chat.id, send.message_id)


@bot.message_handler(content_types=['text'])
def messages(message):
    if message.forward_from is not None:
        if message.forward_from.id == 326394943:
            if message.text.split('\n')[2][0] == '🔵' and 'Снаряжение' in message.text:
                if message.date - message.forward_date < 16:
                    data_base = sqlite3.connect('BB')
                    c = data_base.cursor()
                    c.execute('SELECT tgid FROM accounts')
                    temp = c.fetchone()
                    c.close()
                    data_base.close()
                    if message.from_user.id in temp:
                        pass
                    else:
                        bot.send_message(message.from_user.id, 'Хм.. тебя нет в базе данных, сейчас я тебя '
                                                               'зарегистрирую...')
                        strings = message.text.split('\n', maxsplit=-1)
                        if strings[4][0] == '🛠':
                            user_info = ['tgid', 'name', 'fl', 'wl', 'money', 'nhealth', 'mhealth', 'damage', 'agility',
                                         'agility', 'agility', 'agility']
                            user_info[0] = message.from_user.id
                            user_info[1] = strings[2].split('🔵', maxsplit=1)[1].split(' ')[0]
                            user_info[2] = strings[3].split(': ')[1].split(' ')[0]
                            user_info[3] = strings[4].split(': ')[1].split(' ')[0]
                            user_info[4] = strings[5].split(': ')[1].split(' ')[0]
                            user_info[5] = strings[6].split(' / ')[0].split('❤️ Здоровье: ')[1]
                            user_info[6] = strings[6].split(' / ')[1].split(' ')[0]

                            user_info[7] = strings[7].split('💥 Атака: ')[1].split(' ')[0]
                            if '+' in user_info[7]:
                                user_info[7] = int(user_info[7].split('+')[0]) + int(user_info[7].split('+')[1])

                            user_info[8] = strings[8].split('🛡 Защита: ')[1].split(' ')[0]
                            if '+' in user_info[8]:
                                user_info[8] = int(user_info[8].split('+')[0]) + int(user_info[8].split('+')[1])

                            user_info[9] = strings[9].split('🦎 Ловкость: ')[1].split(' ')[0]
                            if '+' in user_info[9]:
                                user_info[9] = int(user_info[9].split('+')[0]) + int(user_info[9].split('+')[1])

                            user_info[10] = strings[10].split(' / ')[0].split('🔋 Выносливость: ')[1]
                            user_info[11] = strings[10].split(' / ')[1].split(' ')[0]
                        else:
                            user_info = ['tgid', 'name', 'fl', 'wl', 'money', 'nhealth', 'mhealth', 'damage', 'agility',
                                         'agility', 'agility', 'agility']
                            user_info[0] = message.from_user.id
                            user_info[1] = strings[2].split('🔵', maxsplit=1)[1].split(' ')[0]
                            user_info[2] = strings[3].split(': ')[1].split(' ')[0]
                            user_info[3] = 'NULL'
                            user_info[4] = strings[4].split(': ')[1].split(' ')[0]
                            user_info[5] = strings[5].split(' / ')[0].split('❤️ Здоровье: ')[1]
                            user_info[6] = strings[5].split(' / ')[1].split(' ')[0]
                            user_info[7] = strings[6].split('💥 Атака: ')[1].split(' ')[0]
                            if '+' in user_info[7]:
                                user_info[7] = int(user_info[7].split('+')[0]) + int(user_info[7].split('+')[1])
                            user_info[8] = strings[7].split('🛡 Защита: ')[1].split(' ')[0]
                            if '+' in user_info[8]:
                                user_info[8] = int(user_info[8].split('+')[0]) + int(user_info[8].split('+')[1])
                            user_info[9] = strings[8].split('🦎 Ловкость: ')[1].split(' ')[0]
                            if '+' in user_info[9]:
                                user_info[9] = int(user_info[9].split('+')[0]) + int(user_info[9].split('+')[1])
                            user_info[10] = strings[9].split(' / ')[0].split('🔋 Выносливость: ')[1]
                            user_info[11] = strings[9].split(' / ')[1].split(' ')[0]
                        data_base = sqlite3.connect('BB')
                        c = data_base.cursor()
                        c.execute("INSERT INTO accounts (tgid,name,fl,wl,money,nhealth, mhealth,damage, defense, "
                                  "agility, nstamina, mstamina) VALUES ({},'{}',{},{},{},{},{},{},{},{},{},"
                                  "{})".format(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4],
                                               user_info[5], user_info[6], user_info[7], user_info[8], user_info[9],
                                               user_info[10], user_info[11]))
                        data_base.commit()
                        c.close()
                        data_base.close()
                else:
                    bot.send_message(message.from_user.id, 'Ты отправил мне слишком старый форвард!')
            else:
                bot.send_message(message.from_user.id, 'Извини, я пока принимаю только профили, но даже если это и '
                                                       'профиль, то ты скорее всего не из 🔵Синего квартала')
        else:
            bot.send_message(message.from_user.id, 'Извини, но в настоящий момент я только собираю профили.')


bot.polling(none_stop=True, interval=0, timeout=2000000000)
