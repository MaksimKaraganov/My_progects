import sqlite3
import telebot
from telebot import types
import traceback
import random
import datetime

def start_program():
    chat_id = '5209538522' #MAKSIM
    token = 'TOKEN'
    bot = telebot.TeleBot(token)
    #bot.send_message(chat_id=chat_id, text = 'я в строю')

    conn = sqlite3.connect('anekdot.db', check_same_thread=False)
    cursor = conn.cursor()

    numb_day = cursor.execute("select count(Numb) from anekdot_table")
    numb_day = str(cursor.fetchone())
    numb_day = int(numb_day.replace("(", '').replace(",)", ''))
    numb_day = random.randint(1, numb_day)

    @bot.message_handler(commands=['start'])    
    def welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("рандомный анекдот")
        item2 = types.KeyboardButton("наш канал")
        item3 = types.KeyboardButton("анекдот дня")
 
        markup.add(item1, item2, item3)

        
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>🤖, с анекдотами".format(message.from_user, bot.get_me()),
       parse_mode='html', reply_markup=markup)

        get_text_messages(message)

        if " " in message.text:
            referrer_candidate = message.text.split()[1]
            if referrer_candidate != 'admin' and referrer_candidate != 'user_info':
                bot.send_message(message.chat.id, 'Спасибо, что воспользовались рекомандацией @'+ referrer_candidate)
            elif referrer_candidate == 'admin':
                bot.send_message(message.chat.id, 'Добро пожаловать в админ панель')
                admin(message)
            elif referrer_candidate == 'user_info':
                bot.send_message(message.chat.id, 'инфа о пользователях')
                user_info(message)

    @bot.message_handler(content_types=['text'])
    def lalala(message):
        if message.text == 'рандомный анекдот':
            anekdot(message)
        if message.text == 'наш канал':
            msg = bot.send_message(message.from_user.id, 'https://t.me/kornishonchiki')
        if message.text == 'анекдот дня':
            anekdot_day(message)

    def get_text_messages(message): 
        us_id = message.from_user.id 
        info = cursor.execute('SELECT * FROM users WHERE user_id=?', (us_id, )) 
        if info.fetchone() is None: 
            dt = datetime.datetime.now() 
            dt = dt.strftime(dt.strftime("%d-%m-%Y")) 
            us_name = message.from_user.first_name
            us_sname = message.from_user.last_name
            username = message.from_user.username
            db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username, datetime=dt) 

    def db_table_val(user_id: int, user_name: str, user_surname: str, username: str, datetime: str):
        cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username, datetime) VALUES (?, ?, ?, ?, ?)', (user_id, user_name, user_surname, username, datetime))
        conn.commit()

    def anekdot(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("👍")
        item2 = types.KeyboardButton("👎")
 
        markup.add(item1, item2)
        
        numb = cursor.execute("select count(Numb) from anekdot_table")
        numb = str(cursor.fetchone())
        numb = int(numb.replace("(", '').replace(",)", ''))
        numb = random.randint(1, numb)
        anekdot = cursor.execute("SELECT `anekdot` FROM `anekdot_table` WHERE `Numb` = ? ", (numb,))
        msg = bot.send_message(message.chat.id, anekdot, reply_markup=markup)
        msg = bot.send_message(message.chat.id, 'Оцените анекдот')
        bot.register_next_step_handler(message, like, numb)

    def like(message, global_numb):
        like = message.text
        if like == '👍': #обновление рейтинга не работает
            rating = cursor.execute("SELECT `rating` FROM `anekdot_table` WHERE `Numb` = ? ", (global_numb,))
            conn.commit()
            rating = str(cursor.fetchone())
            rating = int(rating.replace("(", '').replace(",)", ''))
            rating = rating+1
            cursor.execute("UPDATE `anekdot_table` SET `rating` = ? WHERE `Numb` = ?", (rating, global_numb)) #не работает вот эта строчка
            conn.commit()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("рандомный анекдот")
        item2 = types.KeyboardButton("наш канал")
        item3 = types.KeyboardButton("анекдот дня")
 
        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, 'Спасибо за оценку', reply_markup=markup)

    def anekdot_day(message):
        anekdot = cursor.execute("SELECT `anekdot` FROM `anekdot_table` WHERE `Numb` = ? ", (numb_day,))
        msg = bot.send_message(message.chat.id, anekdot)

    def admin(message):
        bot.send_message(message.chat.id, 'скинь мне анекдот для добавления')
        bot.register_next_step_handler(message, process_addanekdot_step)
    
    def  process_addanekdot_step(message):
        anekdot = message.text
        anekdot = str(anekdot)
        cursor.execute('INSERT INTO anekdot_table (anekdot, rating) VALUES (?, ?)', (anekdot, 0))
        conn.commit()
        admin(message)

    def user_info(message):
        count_users = cursor.execute("select count(id) from users")
        count_users = str(cursor.fetchone())
        count_users = int(count_users.replace("(", '').replace(",)", ''))
        numb_users = 0
        while numb_users != count_users:
            numb_users = numb_users + 1
            user_id = cursor.execute("SELECT `user_id` FROM `users` WHERE `id` = ? ", (numb_users,))
            user_id = str(cursor.fetchone())
            user_id = user_id.replace("(", '').replace(",)", '')
            user_name = cursor.execute("SELECT `user_name` FROM `users` WHERE `id` = ? ", (numb_users,))
            user_name = str(cursor.fetchone())
            user_name = user_name.replace("(", '').replace(",)", '')
            user_surname = cursor.execute("SELECT `user_surname` FROM `users` WHERE `id` = ? ", (numb_users,))
            user_surname = str(cursor.fetchone())
            user_surname = user_surname.replace("(", '').replace(",)", '')
            username = cursor.execute("SELECT `username` FROM `users` WHERE `id` = ? ", (numb_users,))
            username = str(cursor.fetchone())
            username = username.replace("(", '').replace(",)", '')
            reg_time = cursor.execute("SELECT `datetime` FROM `users` WHERE `id` = ? ", (numb_users,))
            reg_time = str(cursor.fetchone())
            reg_time = reg_time.replace("(", '').replace(",)", '')
            bot.send_message(message.chat.id, f'ID - {user_id}\n Имя - {user_name}\n Фамилия - {user_surname}\n Ник - {username}\n Дата регистрации - {reg_time}')

    bot.polling()

while True:
    try:
        start_program()
    except Exception as e:
        erorr = str(traceback.format_exc())
        print(erorr)