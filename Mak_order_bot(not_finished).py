import telebot
from telebot import types 
import sqlite3 
import datetime
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

user_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Сделать заказ")
item2 = types.KeyboardButton("Устроиться на работу")
item3 = types.KeyboardButton("Обо мне")
user_main.add(item1, item2, item3)

admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Узнать инфу о пользователях")
item2 = types.KeyboardButton("Сделать рассылку")
item3 = types.KeyboardButton("История рассылок")
item4 = types.KeyboardButton("Создать реферальную ссылку")
item5 = types.KeyboardButton("Узнать кол-во рефералов")
item6 = types.KeyboardButton("Перейти в пользовательскую версию")
admin.add(item1, item2, item3, item4, item5, item6)

markup_send = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Отправить")
item2 = types.KeyboardButton("Вернуться в меню")
markup_send.add(item1, item2)

markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Вернуться в меню")
markup_back.add(item1)

grafic = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("5 - 2")
item2 = types.KeyboardButton("2 - 2")
item3 = types.KeyboardButton("Другой случай")
grafic.add(item1, item2, item3)

order_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Бургеры")
item2 = types.KeyboardButton("Завтраки")
item3 = types.KeyboardButton("Комбо наборы")
item4 = types.KeyboardButton("Картофель фри")
item5 = types.KeyboardButton("Салаты и ролы")
item6 = types.KeyboardButton("Десерты")
item7 = types.KeyboardButton("Напитки")
item8 = types.KeyboardButton("Соусы")
order_main.add(item1, item2, item3, item4, item5, item6, item7, item8)

smth_else = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Что-то ещё")
item2 = types.KeyboardButton("Закончить заказ")
smth_else.add(item1, item2)

def main():
    header = Headers(
    headers=True 
    )
    token = 'TOKEN'
    password = 'Admin'
    chat_id = 5209538522
    admin_id = 5209538522#айди администратора или hr 
    grpoup_id = -743773007
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=['start'])    
    def welcome(message):
        if " " in message.text:
            referrer_candidate = message.text.split()[1]
            conn_referrer_add = sqlite3.connect('mac_detabase.db', check_same_thread=False)
            cursor_referrer_add = conn_referrer_add.cursor()
            info = cursor_referrer_add.execute('SELECT * FROM users WHERE user_id=?', (message.from_user.id, )) 
            if info.fetchone() is None: 
                database(message)
                count =  cursor_referrer_add.execute("select `count` from `referal` WHERE `name` = ?",(referrer_candidate,)).fetchone()[0] + 1
                cursor_referrer_add.execute("UPDATE `referal` SET `count` = ? WHERE `name` = ?", (count, referrer_candidate))
                cursor_referrer_add.execute("UPDATE `users` SET `ref_name` = ? WHERE `user_id` = ?", (referrer_candidate, message.from_user.id ))
                conn_referrer_add.commit()
            else:        
                bot.send_message(chat_id, f'Перешёл по реферальной ссылке, хотя пользовался ботом ранее {message.from_user.id}\n @{message.from_user.username}')
                conn_referrer_add.close()
                bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>🤖, бот для заказов во Вкусно-и точка".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=user_main)
        else:
            database(message)
            bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>🤖, бот для заказов во Вкусно-и точка".format(message.from_user, bot.get_me()),
       parse_mode='html', reply_markup=user_main)

    @bot.message_handler(content_types=['text'])
    def main_menu(message):
        if message.text == 'Сделать заказ':
            user_order = []
            bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=order_main)
            bot.register_next_step_handler(message, order, user_order)
        elif message.text == 'Устроиться на работу': #регистрация узнать где ты живёшь
            bot.send_message(message.from_user.id, 'Пришлите пожалуйста ссылку на выше резюме')
            bot.register_next_step_handler(message, new_resume)
        elif message.text == 'Обо мне':
            bot.send_message(message.from_user.id, 'Я помогу тебе сделать заказ быстро и удобно')
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=user_main)

        elif message.text == password and (message.chat.id == chat_id ):
            bot.send_message(message.from_user.id, 'Добро пожаловать в админ панель', reply_markup=admin)
        elif message.text == 'Узнать инфу о пользователях' and (message.chat.id == chat_id ):
            conn_us_info = sqlite3.connect('mac_detabase.db', check_same_thread=False)
            cursor_us_info = conn_us_info.cursor()
            users = cursor_us_info.execute("select * from `users`").fetchall()
            conn_us_info.close()
            for row in users:
                bot.send_message(message.chat.id, f'ID - {row[0]}\n Имя - {row[1]}\n Фамилия - {row[2]}\n Ник - {row[3]}\n Дата регистрации - {row[4]}\n Реферал - {row[5]}')
            bot.send_message(message.chat.id, 'Это все пользователи на сегодня')
        elif message.text == 'Сделать рассылку' and (message.chat.id == chat_id ):
            bot.send_message(message.chat.id, 'Пришлите пожалуйста текст рассылки')
            bot.register_next_step_handler(message, rassilka_step)
        elif message.text == 'История рассылок' and (message.chat.id == chat_id ):
            conn_basa_rassilka = sqlite3.connect('mac_detabase.db', check_same_thread=False)
            cursor_basa_rassilka = conn_basa_rassilka.cursor()
            bot.send_message(message.chat.id, 'История рассылок')
            sended = cursor_basa_rassilka.execute("select * from `basa_rassilka`").fetchall()
            conn_basa_rassilka.close()
            for row in sended:
                try:
                    bot.send_photo(message.chat.id, row[1], caption=f'📝{row[0]}\n⏱{row[2]}')
                except:
                    bot.send_message(message.chat.id, f'📝{row[0]}\n⏱{row[2]}')
        elif message.text == 'Создать реферальную ссылку' and (message.chat.id == chat_id ):
            bot.send_message(message.from_user.id, 'Введите имя на английском')
            bot.register_next_step_handler(message, referali_create)
        elif message.text == 'Узнать кол-во рефералов' and (message.chat.id == chat_id ):
            ref_info(message)
        elif message.text == 'Перейти в пользовательскую версию' and (message.chat.id == chat_id ):
            bot.send_message(message.chat.id, 'Добро пожаловать в пользовательскую версию', reply_markup=user_main)
        
        elif message.text == 'GEO':
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
            keyboard.add(button_geo)
            bot.send_message(message.from_user.id, 'GEO', reply_markup=keyboard)
            bot.register_next_step_handler(message, geo)

        else:
            bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку')

    @bot.callback_query_handler(func=lambda call: True)
    def answer(call):#выкинуть нахер
        if call.data == 'answer_from_chat':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=call.message.text, reply_markup=None)
            bot.send_message(call.message.chat.id,
                         call.from_user.first_name + '(@' + call.from_user.username + ')' + ' Взял заказ')
            order_text=call.message.text.replace("Новый заказ ", '')
            conn_order_update = sqlite3.connect('mac_detabase.db', check_same_thread=False)
            cursor_order_update = conn_order_update.cursor()
            cursor_order_update.execute("UPDATE `order` SET `worker_id` = ?, `worker_tag` = ?, `status` = ?  WHERE `order_info` = ?", (call.from_user.id, call.from_user.username, 'Took', order_text))
            conn_order_update.commit()
            conn_order_update.close()

    def geo(message):
        bot.send_message(message.chat.id,message.location.longitude)
        bot.send_message(message.chat.id,message.location.latitude, reply_markup=user_main)

    def order(message, user_order):
        if message.text == 'Бургеры':
            menu = 'burgers'
            send_meny(message, menu, user_order)
        elif message.text == 'Завтраки':
            menu = 'zavtrak'
            send_meny(message, menu, user_order)
        elif message.text == 'Комбо наборы':
            menu = 'makkombo'
            send_meny(message, menu, user_order)
        elif message.text == 'Картофель фри':
            menu = 'kartofel-i-startery'
            send_meny(message, menu, user_order)
        elif message.text == 'Салаты и ролы':
            menu = 'salaty-i-rolly'
            send_meny(message, menu, user_order)
        elif message.text == 'Десерты':
            menu = 'deserty-i-vypechka'
            send_meny(message, menu, user_order)
        elif message.text == 'Напитки':
            menu = 'napitki-i-koktejli'
            send_meny(message, menu, user_order)
        elif message.text == 'Соусы':
            menu = 'sousy'
            send_meny(message, menu, user_order)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=user_main)
        else:
            bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку')
            bot.register_next_step_handler(message, order, user_order)

    def send_meny(message, menu, user_order):
        link = f'https://vkusnoitchka.ru/{menu}/'
        user_agent = header.generate()
        response = requests.get(link, headers=user_agent)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml') 
        burgers = soup.findAll('div', class_='h5')
        photoes = soup.find_all('div', class_='item-image')
        counter = 0
        food = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for photo in photoes:
            photo = photo.img['data-lazy-src'].replace("-465x465",'')
            bot.send_photo(message.from_user.id, photo, caption=burgers[counter].text)
            item = types.KeyboardButton(f'{burgers[counter].text}')
            food.add(item)
            counter = counter + 1
        bot.send_message(message.from_user.id, 'Что будете сегодня?', reply_markup=food)
        bot.register_next_step_handler(message, order_from_user, user_order)

    def order_from_user(message, user_order):
        user_order.append(message.text)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=smth_else)
        bot.register_next_step_handler(message, order_from_user_else_step, user_order)
    
    def order_from_user_else_step(message, user_order):
        if message.text == 'Что-то ещё':
            bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=order_main)
            bot.register_next_step_handler(message, order, user_order)
        if message.text == 'Закончить заказ':
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton( text='Взять',  callback_data='answer_from_chat')
            markup.add(btn)
            bot.send_message(message.from_user.id, f"Спасибо за заказ", reply_markup=user_main)
            bot.send_message(grpoup_id, f"Новый заказ {user_order}", reply_markup=markup)
            conn_order = sqlite3.connect('mac_detabase.db', check_same_thread=False)
            cursor_order = conn_order.cursor()
            cursor_order.execute('INSERT INTO `order`(order_info, user_id, user_tag) VALUES (?, ?, ?)', (str(user_order), message.from_user.id, message.from_user.username))
            conn_order.commit()
            conn_order.close()

    def new_resume(message):
        link_on_resume = message.text
        bot.send_message(message.chat.id, 'Выберите график работы в котором бы вы хотели работать', reply_markup=grafic)
        bot.register_next_step_handler(message, new_send_admin, link_on_resume)

    def new_send_admin(message, link_on_resume):
        grafic = message.text
        bot.send_message(message.chat.id, 'Спасибо, что оставили заявку', reply_markup=user_main)
        bot.send_message(admin_id, f'Заявка на работу\nссылка на резюме: {link_on_resume}\n желаемый график работы: {grafic}')

    def rassilka_step(message):
        message_important = message
        bot.send_message(message.chat.id, 'Вы уверены что отправить?', reply_markup= markup_send)
        bot.register_next_step_handler(message, rassilka, message_important)
        
    def rassilka(message, message_important):
        if message.text == 'Отправить':
            try:
                conn_rassilka = sqlite3.connect('mac_detabase.db', check_same_thread=False)
                cursor_rassilka = conn_rassilka.cursor()
                idphoto = 0
                message = message_important
                dt = datetime.datetime.now() 
                dt = dt.strftime(dt.strftime("Day: %d/%m/%Y  time: %H:%M:%S"))
                users_id = cursor_rassilka.execute("select `user_id` from `users`").fetchall()
                try:
                    idphoto = message.photo[0].file_id
                    text = message.caption
                    for row in users_id:
                        try:
                            bot.send_photo(row[0], idphoto, caption = text)
                        except:
                            bot.send_message(message.chat.id, f'Добавил в чс - {row[0]}')
                except:
                    text = message.text
                    for row in users_id:
                        try:
                            bot.send_message(row[0], text)
                        except:
                            bot.send_message(message.chat.id, f'Добавил в чс - {row[0]}')
                bot.send_message(message.chat.id, 'рассылка произошла успешно', reply_markup = admin)
                cursor_rassilka.execute('INSERT INTO basa_rassilka (text, photo, data) VALUES (?, ?, ?)', (text, idphoto, dt))
                conn_rassilka.commit()
                conn_rassilka.close()
                bot.send_message(message.chat.id, 'рассылка сохранена')
            except:
                bot.send_message(message.chat.id, 'произошла ошибка', reply_markup = admin)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup = admin)
        else:
            bot.send_message(message.chat.id, 'нажмите пожалуйста на кнопку')
            bot.register_next_step_handler(message, rassilka, message_important)

    def referali_create(message):
        name = message.text
        if name != 'Вернуться в меню':
            conn_referali_create = sqlite3.connect('mac_detabase.db', check_same_thread=False)
            cursor_referali_create = conn_referali_create.cursor()
            info = cursor_referali_create.execute('SELECT * FROM referal WHERE name=?', (name, )) 
            if info.fetchone() is None: 
                cursor_referali_create.execute('INSERT INTO referal (name, count) VALUES (?, ?)', (name, 0))
                conn_referali_create.commit()
                bot.send_message(message.chat.id, f'https://t.me/Armany_by_maks_bot?start={name}\n \nваша ссылка успешно создана')
            else:
                bot.send_message(message.chat.id, f'Имя уже занято, по пробуйте другое')
                bot.register_next_step_handler(message, referali_create)
            conn_referali_create.close()
        else:
            bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=admin)

    def ref_info(message):
        conn_ref_info = sqlite3.connect('mac_detabase.db', check_same_thread=False)
        cursor_ref_info = conn_ref_info.cursor()
        referal = cursor_ref_info.execute("select * from `referal`").fetchall()
        conn_ref_info.close()
        for row in referal:
            bot.send_message(message.chat.id, f'Имя ссылки - {row[0]}\n Колличество переходов - {row[1]}\n сама ссылка - https://t.me/AliExprssSearch_bot?start={row[0]}')
        bot.send_message(message.chat.id, 'Это все ваши реферальные ссылки')  

    def database(message):
        conn_add_user = sqlite3.connect('mac_detabase.db', check_same_thread=False)
        cursor_add_user = conn_add_user.cursor()
        info = cursor_add_user.execute('SELECT * FROM users WHERE user_id=?', (message.from_user.id, )) 
        if info.fetchone() is None: 
            dt = datetime.datetime.now() 
            dt = dt.strftime(dt.strftime("%d-%m-%Y"))
            cursor_add_user.execute('INSERT INTO users (user_id, user_name, user_surname, username, datetime) VALUES (?, ?, ?, ?, ?)', (message.from_user.id , message.from_user.first_name, message.from_user.last_name, message.from_user.username, dt))
            conn_add_user.commit()
        conn_add_user.close()

    bot.polling()

if __name__ == '__main__':
    main()