#!/usr/bin/python3
# -*- coding: utf-8 -*-
import telebot
from telebot import types

admin_list = [391545947, 64000151, 121485043, 339824315]
token = '462200530:AAE-0tbERzSSKg_lsNz_x-Gvlw9ItITejvY'
bot = telebot.TeleBot(token)


@bot.inline_handler(lambda query: query.query == 'Защита')
def query_text(inline_query):
    if inline_query == 'Защита':
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


bot.polling(none_stop=True, interval=0, timeout=2000000000)

"""
"""

"""
cost_pp = 31
cost_umbrl = 25
cost_hooli = 30
cost_stark = 39
cost_wayne = 95

capital_pp = 456794
capital_umbrl = 637427
capital_hooli = 559190
capital_stark = 511246
capital_wayne = 302670

daily_income_pp = 26942
daily_income_umbrl = 30248
daily_income_hooli = 28750
daily_income_stark = 26639
daily_income_wayne = 29231

count_actions_pp = capital_pp/cost_pp
count_actions_umbrl = capital_umbrl/cost_umbrl
count_actions_hooli = capital_hooli/cost_hooli
count_actions_stark = capital_stark/cost_stark
count_actions_wayne = capital_wayne/cost_wayne

dividends_pp = (0.375*daily_income_pp)/count_actions_pp
dividends_umbrl = (0.375*daily_income_umbrl)/count_actions_umbrl
dividends_hooli = (0.375*daily_income_hooli)/count_actions_hooli
dividends_stark = (0.375*daily_income_stark)/count_actions_stark
dividends_wayne = (0.375*daily_income_wayne)/count_actions_wayne

print ("pp - " + str(dividends_pp))
print ("umbrella - " + str(dividends_umbrl))
print ("hooli - " + str(dividends_hooli))
print ("stark - " + str(dividends_stark))
print ("wayne - " + str(dividends_wayne))
"""
