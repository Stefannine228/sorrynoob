import telebot
import sqlite3
from telebot import types

name =''

bot = telebot.TeleBot("6880422905:AAFSSfSh38NxEyluwZglfCKivX9b2zp_6g8")

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("/start")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, 'Hello \n /start - запуск бота \n /help - всі команди', reply_markup=markup)
    #bot.register_next_step_handler(message, on_click)
#def on_click(message):
#    if message.text == 'help':
 #       bot.send_message(message.chat.id, '/start - запуск бота \n /help - всі команди \n /info - інформація про користувача \n /imba - імба\n\n додатковий функціонал: \n "хто підор" дає відповідь на запитання')
  #  elif message.text == 'start':
   #     markup = types.ReplyKeyboardMarkup()
    #    btn1 = types.KeyboardButton("help")
     #   btn2 = types.KeyboardButton("start")
      #  markup.row(btn1, btn2)
       # bot.send_message(message.chat.id, 'Hello \n /start - запуск бота \n /help - всі команди', reply_markup=markup)
        #bot.register_next_step_handler(message, on_click)
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '/start - запуск бота \n /help - всі команди \n /info - інформація про користувача \n /imba - імба \n /pashalko - відправляє рандомну пасхалку \n\n додатковий функціонал: \n "хто підор" дає відповідь на запитання')
    markup = types.ReplyKeyboardMarkup()
    start = KeyboardButton('/start')
    help1 = KeyboardButton('/help')
    randompshalko = KeyboardButton('/pashalko')

@bot.message_handler(commands=['pashalko'])
def main(message):
    file = open('./fan.png','rb')
    bot.send_photo(message.chat.id, file)

@bot.message_handler(commands=['delete'])
def main(message):
    bot.delete_message(message.chat.id, message.message_id-1)
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, message)
@bot.message_handler(commands=['imba'])
def photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("так", callback_data='btn1', url='https://images.prom.ua/5148298037_w600_h600_5148298037.jpg')
    btn2 = types.InlineKeyboardButton("звичайно", callback_data='btn2', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'хочеш побачити імбу', reply_markup=markup)

@bot.message_handler(commands=['test_button'])
def start_command(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("delete", callback_data='btn11')
    btn2 = types.InlineKeyboardButton("edit", callback_data='btn12')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Тестові кнопки", reply_markup=markup)


@bot.message_handler(commands=['sqlite'])
def main(message):
    conn = sqlite3.connect('file.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(8))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Проводиться регестрація. Введіть імя')
    bot.register_next_step_handler(message, user_name)



def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Проводиться регестрація. Введіть пароль')
    bot.register_next_step_handler(message, user_pass)
def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('file.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, pass) VALUES('%s','%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список користувачів', callback_data='users'))

    bot.send_message(message.chat.id, 'Регестрація завершена!', reply_markup=markup)


@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    conn = sqlite3.connect('file.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Імя: {el[1]}, пароль: {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback1):
    if callback.data == 'btn11':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'btn12':
        bod.edit.message_text('Edit text',callback.message.chat.id, callback.message.message_id)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'хто підор':
        bot.send_message(message.chat.id, f'{message.chat.username} підор')

bot.infinity_polling()