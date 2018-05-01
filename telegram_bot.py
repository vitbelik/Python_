import requests
import config
import exmo
import time
import telebot
import json, ast
from  telebot import types

token = config.token
URL = 'https://api.telegram.org/bot' + token + '/'
bot = telebot.TeleBot(config.token)

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)

    return r.json()


# def proc_json():
#     d = get_updates()
#     with open('updates.json', 'w') as file:
#         json.dump(d, file, indent=2 )

def get_last_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    text = data['result'][-1]['message']['text']

    message = {'chat_id': chat_id,
               'message': text}
    return message


def sent_message(ch_id, text='Wait a second please...'):
    url = URL + 'sendmessage?chat_id={0}&text={1}'.format(ch_id, text)
    r = requests.get(url)
    return r.json()




@bot.message_handler(content_types='text')
def handle_command(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('d')
    btn2 = types.KeyboardButton('h')
    btn3 = types.KeyboardButton('r')
    a = types.KeyboardButton('l')
    c = types.KeyboardButton('0')
    markup.add(btn1, btn2, btn3, a, c)
    bot.send_message('172570721', 'Choose', reply_markup=markup)
    print('Command was received')


bot.polling(none_stop=True, interval=0)


# def main():
#     # while True:
#         last_message = get_last_message()
#         chat_id = last_message['chat_id']
#         text = last_message['message']
#         print(chat_id)
#
#
#         if text == '/start':
#              sent_message(chat_id, 'Привет! Я бот В-ка! Напишу какую инфу ты хочешь получать?')
#         elif text[1:] in exmo.valytu:
#             sent_message(chat_id, str(exmo.get_usd(exmo.valytu[text[1:]], 'buy_price')))
#         else:
#             sent_message(chat_id, 'Короче...')
#
#         time.sleep(3)
#
#
# if __name__ == '__main__':
#     main()