import sqlite3
import telebot
from telebot import types
import mesh
import traceback
import datetime

def start_program():
    chat_id = '5209538522' #MAKSIM
    token = 'TOKEN'
    bot = telebot.TeleBot(token)
    bot.send_message(chat_id=chat_id, text = 'я в строю')

    conn = sqlite3.connect('users.db', check_same_thread=False)
    cursor = conn.cursor()

    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🤖Цдз🤖")
    item3 = types.KeyboardButton("💰Донаты💰")
    item4 = types.KeyboardButton("Профиль")
    item5 = types.KeyboardButton("Информация о боте")
    item6 = types.KeyboardButton("Поддержка")
    markup_menu.add(item1, item3, item4, item5, item6)

    markup_try = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Попробовать")
    item2 = types.KeyboardButton("Вернуться")
    markup_try.add(item1, item2)
 

    def db_table_val(user_id: int, user_name: str, user_surname: str, username: str, datetime: str):
        cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username, datetime) VALUES (?, ?, ?, ?, ?)', (user_id, user_name, user_surname, username, datetime))
        conn.commit()

    def get_text_messages(message):
        us_id = message.from_user.id
        info = cursor.execute('SELECT * FROM users WHERE user_id=?', (us_id, ))
        if info.fetchone() is None: 
            dt = datetime.datetime.now()
            dt = dt.strftime(dt.strftime("%d-%m-%Y"))
            us_name = message.from_user.first_name
            us_sname = message.from_user.last_name
            username = message.from_user.username
            bot.send_message(message.chat.id, f'👤 Никнейм: - @{message.from_user.username} \n'
                         + f'Ваше имя  -  {message.from_user.first_name} \n'
                         +f'🔑 ID: - {message.chat.id} \n' 
                         +f'🗓 Начало использования бота - {dt}\n'
                         +f'Ваша реферальная ссылка - https://t.me/VM_international_bot?start={message.from_user.username}')
            db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username, datetime=dt)
        else:
            user_id = message.from_user.id
            reg_time = cursor.execute("SELECT `datetime` FROM `users` WHERE `user_id` = ? ", (user_id,))
            reg_time = cursor.fetchone()[0]
            bot.send_message(message.chat.id, f'👤 Никнейм: - @{message.from_user.username} \n'
                         + f'Ваше имя  -  {message.from_user.first_name} \n'
                         +f'🔑 ID: - {message.chat.id} \n' 
                         +f'🗓 Начало использования бота - {reg_time}\n'
                         +f'Ваша реферальная ссылка - https://t.me/VM_international_bot?start={message.from_user.username}' )

    @bot.message_handler(commands=['start'])    
    def welcome(message):
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>🤖, бот который умеет решать тесты МЭШ".format(message.from_user, bot.get_me()),
       parse_mode='html', reply_markup=markup_menu)
        if " " in message.text:
            referrer_candidate = message.text.split()[1]
            bot.send_message(message.chat.id, 'Спасибо, что воспользовались рекомандацией @'+ referrer_candidate)
        #try:
         #  print(referrer_candidate)
            #(запись реферала в базу данных)

    @bot.message_handler(content_types=['text'])
    def lalala(message):
        if message.text == '🤖Цдз🤖':
            msg = bot.send_message(message.from_user.id, 'кинь мне ссылку', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, process_name_step)
        if message.text == '✍️Конспектор✍️':
            msg = bot.send_message(message.from_user.id, 'в разработке')
        if message.text =='💰Донаты💰':
            msg = bot.send_message(message.from_user.id, 'Если хотите поддержать проект перейдите по ссылке qiwi.com/n/NOMIN843')
        if message.text =='Профиль':
            get_text_messages(message)
        if message.text == 'Информация о боте':
            msg = bot.send_message(message.from_user.id, 'Помогалыч - это бот созданный VM production💻 \n Умеет решать тесты МЭШ \n Разработчик проекта - @Byg0r_Maksim \n Идейный генератор проекта - @Chebupela_777 \n Наш телеграмм канал https://t.me/VMproduct')
        if message.text == 'Поддержка':
            msg = bot.send_message(message.from_user.id, 'тебе туда-> @Chebupela_777')

    def process_name_step(message):
        try:
            us_id = message.from_user.id
            name = message.text
            answers = mesh.get_answers(name)
            for task_number, task in enumerate(answers):
                bot.send_message (message.chat.id, text = "❓- вопрос %d: %s" % (task_number + 1, task [0]))
                bot.send_message (message.chat.id, text = "\t✍️- ответы: %s\n" % task [1])
            bot.send_message(message.chat.id, 'Тест решен',  reply_markup=markup_menu)
        except Exception as e:
            bot.reply_to(message, 'c этой ссылкой чото не так')
            bot.send_message(message.chat.id, 'Побруете скинуть снова?', reply_markup=markup_try)
            bot.register_next_step_handler(message, process_age_step)

    def process_age_step(message):
        try:
            if message.text == 'Попробовать':
                msg = bot.send_message(message.from_user.id, 'кинь мне ссылку', reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, process_name_step)
            elif message.text == 'Вернуться':
                bot.send_message(message.chat.id, "Вы в начальном меню🌐", reply_markup=markup_menu)
        except Exception as e:
            bot.send_message(message.chat.id, 'что-то пошло не так(')
    bot.polling()

while True:
    try:
        start_program()
    except Exception as e:
        erorr = str(traceback.format_exc())
        print(erorr)