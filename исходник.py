import telebot #отвечает за связь с телеграм
from telebot import types #отвечает за связь с телеграм
import sqlite3 #отвечает за работу с бд
from bs4 import BeautifulSoup #с помощью него вытаскиваю данные из полученного html
from threading import Thread #даёт асинхронность (например проверять время чтобы запустить функцию в 0.00)
import schedule #запускает функцию в 0.00
import undetected_chromedriver as uc #управление физическим браузером
import datetime #помогает получить реальное время
import time #отвечает за действия со временем условно отложить на 5 сек
import random #рандом
import settings #настройки
import traceback
#основная клавиатура пользователя
user_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Выбрать категорию товара")
item2 = types.KeyboardButton("Рандомный товар")
item3 = types.KeyboardButton("О нас")
user_main.add(item1, item2, item3)
#основная клавиатура админа
admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Добавить товары")
item2 = types.KeyboardButton("Узнать инфу о пользователях")
item3 = types.KeyboardButton("Проверить актуальность цен")
item4 = types.KeyboardButton("Сделать рассылку")
item5 = types.KeyboardButton("История рассылок")
item6 = types.KeyboardButton("Создать реферальную ссылку")
item7 = types.KeyboardButton("Узнать кол-во рефералов")
item8 = types.KeyboardButton("Удалить товар")
item9 = types.KeyboardButton("Перейти в пользовательскую версию")
admin.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
#мужские категории товаров
category = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Футболки")
item2 = types.KeyboardButton("Штаны")
item3 = types.KeyboardButton("Кофты")
item4 = types.KeyboardButton("Бижутерия")
item5 = types.KeyboardButton("Бомберы")
item6 = types.KeyboardButton("Кепки")
item7 = types.KeyboardButton("Шапки")
item8 = types.KeyboardButton("Шорты")
item9 = types.KeyboardButton("Очки")
item10 = types.KeyboardButton("Сумки")
item11 = types.KeyboardButton("Рубашки")
item12 = types.KeyboardButton("Обувь")
item13 = types.KeyboardButton("Ночники")
item14 = types.KeyboardButton("Свитера")
item15 = types.KeyboardButton("Куртки")
item16 = types.KeyboardButton("Ветровки")
item17 = types.KeyboardButton("Пальто")
item18 = types.KeyboardButton("Шарфы")
item19 = types.KeyboardButton("Аниме")
item20 = types.KeyboardButton("1000мелочей")
item21 = types.KeyboardButton("Вернуться в меню")
category.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21)
#женские категории товаров
category_girls = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Футболки")
item2 = types.KeyboardButton("Штаны")
item3 = types.KeyboardButton("Кофты")
item4 = types.KeyboardButton("Бижутерия")
item5 = types.KeyboardButton("Свитера")
item6 = types.KeyboardButton("Кепки")
item7 = types.KeyboardButton("Шапки")
item8 = types.KeyboardButton("Аниме")
item9 = types.KeyboardButton("Очки")
item10 = types.KeyboardButton("Сумки")
item11 = types.KeyboardButton("Рубашки")
item12 = types.KeyboardButton("Обувь")
item13 = types.KeyboardButton("Ночники")
item14 = types.KeyboardButton("Перчатки")
item15 = types.KeyboardButton("Куртки")
item16 = types.KeyboardButton("Кардиганы")
item17 = types.KeyboardButton("Пижамы")
item18 = types.KeyboardButton("Рюкзаки")
item19 = types.KeyboardButton("Топы")
item20 = types.KeyboardButton("Платья")
item21 = types.KeyboardButton("Юбки")
item22 = types.KeyboardButton("Колготки")
item23 = types.KeyboardButton("Спорттовары")
item24 = types.KeyboardButton("Чокеры")
item25 = types.KeyboardButton("1000мелочей")
item26 = types.KeyboardButton("Вернуться в меню")
category_girls.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26)
#выбор мужских или женских товаров
girl_boy_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Мужской")
item2 = types.KeyboardButton("Женский")
item3 = types.KeyboardButton("Вернуться в меню")
girl_boy_key.add(item1, item2, item3)
#просмотр вещей
markup_watch = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Вернуться в меню")
item2 = types.KeyboardButton("Смотреть ещё")
markup_watch.add(item1, item2)
#отправка рассылки
markup_send = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Отправить")
item2 = types.KeyboardButton("Вернуться в меню")
markup_send.add(item1, item2)
#просто возврат в меню используется когда нет другой клавиаутры
markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Вернуться в меню")
markup_back.add(item1)
#на случай отсутсвия ценовых категорий
markup_back_prise = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Смотреть все")
item2 = types.KeyboardButton("Вернуться в меню")
markup_back_prise.add(item1, item2)
#ценовая категория футболка
prise_fytbolka = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("500 - 1200")
item2 = types.KeyboardButton("1200 - 1600")
item3 = types.KeyboardButton("1600+")
item4 = types.KeyboardButton("Смотреть все")
item5 = types.KeyboardButton("Вернуться в меню")
prise_fytbolka.add(item1, item2, item3, item4, item5)
#ценовая категория кофта
prise_koft = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("500 - 1500")
item2 = types.KeyboardButton("1500 - 2200")
item3 = types.KeyboardButton("2200+")
item4 = types.KeyboardButton("Смотреть все")
item5 = types.KeyboardButton("Вернуться в меню")
prise_koft.add(item1, item2, item3, item4, item5)
#ценовая категория штаны
prise_shtani = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("500 - 1500")
item2 = types.KeyboardButton("1500 - 2500")
item3 = types.KeyboardButton("2500+")
item4 = types.KeyboardButton("Смотреть все")
item5 = types.KeyboardButton("Вернуться в меню")
prise_shtani.add(item1, item2, item3, item4, item5)
#начало программы
subscribe_man = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton(text='Проверить подписку',  callback_data='Check_man')
subscribe_man.add(btn)

subscribe_girl = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton(text='Проверить подписку',  callback_data='Chek_girl')
subscribe_girl.add(btn)

def start_program():
    #обьявление айди админов
    chat_id = 1949227825
    chat_id_Maksim = 5209538522
    id_admin_1 = settings.id_admin_1
    id_admin_2 = settings.id_admin_2
    id_admin_3 = settings.id_admin_3
    id_admin_4 = settings.id_admin_4
    id_admin_5 = settings.id_admin_5
    password = settings.password
    #подключение к боту телеграм
    token = settings.token
    bot = telebot.TeleBot(token)
    #сообщает мне пароль(могу убрать), но в целом я знаю когда ты его запускаешь
    bot.send_message(chat_id_Maksim, f'Бот запущен пароль от бота - {password}')
    @bot.message_handler(commands=['start'])    
    def welcome(message):
    #если есть реферальная часть
        if " " in message.text:
            referrer_candidate = message.text.split()[1]
            #проверка пароля и айди пользоватля
            if referrer_candidate == password and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
                #провекра есть-ли пользователь в базе и если что добавление
                database(message)
                bot.send_message(message.chat.id, 'Добро пожаловать в админ панель', reply_markup=admin)
            #если нет пароля
            else:
                #запись как реферала и как пользователя
                referrer_add(message, referrer_candidate)
                bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>🤖, бот c крутыми товарами AliExpress'а ".format(message.from_user, bot.get_me()),
       parse_mode='html', reply_markup=user_main)
        else:
            #при отсутвии реферальной части добавление в базу
            database(message)
            bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>🤖, бот c крутыми товарами AliExpress'а ".format(message.from_user, bot.get_me()),
       parse_mode='html', reply_markup=user_main)
    #меню приходит сюда
    @bot.message_handler(content_types=['text'])
    def lalala(message):
        if message.text == 'Выбрать категорию товара':
            bot.send_message(message.chat.id, 'Какого вы пола?', reply_markup=girl_boy_key)
            bot.register_next_step_handler(message, girl_boy_step)
        elif message.text == 'Рандомный товар': 
            conn_random = sqlite3.connect('database.db', check_same_thread=False)
            cursor_random = conn_random.cursor()
            reiting = '0'
            tovar = cursor_random.execute("select * from `tovar` WHERE `reiting` != ?", (reiting,)).fetchall()
            conn_random.close()
            numb = random.randint(0, len(tovar)-1)
            bot.send_photo(message.chat.id, tovar[numb][5], caption=f'💸{tovar[numb][1]}\n🌟{tovar[numb][2]}/5\n🛒{tovar[numb][3]}\n~ {tovar[numb][4]}')
        elif message.text == 'О нас':
            bot.send_message(message.from_user.id, 'Наш мужской канал - https://t.me/hypewear22\nНаш женский канал - https://t.me/yummyAliExpress\nМы в VK - https://vk.com/hypewear2022\nПо всем вопросам - @jesbycvv')
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=user_main)

        elif message.text == password and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            bot.send_message(message.from_user.id, 'Добро пожаловать в админ панель', reply_markup=admin)
        elif message.text == 'Добавить товары' and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            bot.send_message(message.chat.id, 'Товар мужской или женский?', reply_markup=girl_boy_key)
            bot.register_next_step_handler(message, add_tovar_girl_boy_step)
        elif message.text == 'Узнать инфу о пользователях' and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            conn_us_info = sqlite3.connect('database.db', check_same_thread=False)
            cursor_us_info = conn_us_info.cursor()
            users = cursor_us_info.execute("select * from `users` WHERE `reiting` != ?").fetchall()
            conn_us_info.close()
            for row in users:
                bot.send_message(message.chat.id, f'ID - {row[0]}\n Имя - {row[1]}\n Фамилия - {row[2]}\n Ник - {row[3]}\n Дата регистрации - {row[4]}\n Реферал - {row[5]}')
            bot.send_message(message.chat.id, 'Это все пользователи на сегодня')
        elif message.text == 'Проверить актуальность цен' and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            chek_alik(message)
        elif message.text == 'Сделать рассылку' and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            bot.send_message(message.chat.id, 'Пришлите пожалуйста текст рассылки')
            bot.register_next_step_handler(message, rassilka_step)
        elif message.text == 'История рассылок' and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            conn_basa_rassilka = sqlite3.connect('database.db', check_same_thread=False)
            cursor_basa_rassilka = conn_basa_rassilka.cursor()
            bot.send_message(message.chat.id, 'История рассылок')
            sended = cursor_basa_rassilka.execute("select * from `basa_rassilka`").fetchall()
            conn_basa_rassilka.close()
            for row in sended:
                try:
                    bot.send_photo(message.chat.id, row[1], caption=f'📝{row[0]}\n⏱{row[2]}')
                except:
                    bot.send_message(message.chat.id, f'📝{row[0]}\n⏱{row[2]}')
        elif message.text == 'Создать реферальную ссылку' and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            bot.send_message(message.from_user.id, 'Введите значение на английском')
            bot.register_next_step_handler(message, referali_create)
        elif message.text == 'Узнать кол-во рефералов' and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            conn_ref_info = sqlite3.connect('database.db', check_same_thread=False)
            cursor_ref_info = conn_ref_info.cursor()
            referal = cursor_ref_info.execute("select * from `referal`").fetchall()
            conn_ref_info.close()
            for row in referal:
                bot.send_message(message.chat.id, f'Имя ссылки - {row[0]}\n Колличество переходов - {row[1]}\n сама ссылка - https://t.me/AliExprssSearch_bot?start={row[0]}')
            bot.send_message(message.chat.id, 'Это все ваши реферальные ссылки')  
        elif message.text == 'Перейти в пользовательскую версию' and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            bot.send_message(message.chat.id, 'Добро пожаловать в пользовательскую версию', reply_markup=user_main)
        elif message.text == 'Удалить товар' and (message.chat.id == chat_id or message.chat.id == chat_id_Maksim or message.chat.id == id_admin_1 or message.chat.id == id_admin_2 or message.chat.id == id_admin_3 or message.chat.id == id_admin_4 or message.chat.id == id_admin_5):
            bot.send_message(message.chat.id, 'Пришлите ссылку на товар', reply_markup=markup_back)
            bot.register_next_step_handler(message, delet_tovar)
        else:
            bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку')

    def delet_tovar(message):
        if message.text != 'Вернуться в меню':
            try:
                link = message.text
                con_delet_tovar = sqlite3.connect('database.db', check_same_thread=False)
                cursor_delet_tovar = con_delet_tovar.cursor()
                cursor_delet_tovar.execute("DELETE FROM `tovar` WHERE `link` = ?", (link,))
                con_delet_tovar.commit()
                con_delet_tovar.close()
                bot.send_message(message.chat.id, 'Товар удалён', reply_markup=admin)
            except Exception:
                bot.send_message(chat_id, traceback.format_exc())
                bot.send_message(message.chat.id, 'Произошла ошибка при удалении товара', reply_markup=admin)
        else:
            bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=admin)

    def referali_create(message):
        name = message.text
        if name != 'Вернуться в меню':
            conn_referali_create = sqlite3.connect('database.db', check_same_thread=False)
            cursor_referali_create = conn_referali_create.cursor()
            info = cursor_referali_create.execute('SELECT * FROM referal WHERE name=?', (name, )) 
            if info.fetchone() is None: 
                cursor_referali_create.execute('INSERT INTO referal (name, count) VALUES (?, ?)', (name, 0))
                conn_referali_create.commit()
                bot.send_message(message.chat.id, f'https://t.me/AliExprssSearch_bot?start={name}\n \nваша ссылка успешно создана')
            else:
                bot.send_message(message.chat.id, f'Имя уже занято, по пробуйте другое')
                bot.register_next_step_handler(message, referali_create)
            conn_referali_create.close()
        else:
            bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=admin)
          
    def referrer_add(message, referrer_candidate):
        conn_referrer_add = sqlite3.connect('database.db', check_same_thread=False)
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
    
    def check_sub_channel(chat_member):
        if chat_member.status == 'left':
            return True
        else:
            return False

    @bot.callback_query_handler(func=lambda call: True)
    def answer(call):
        if call.data == 'Check_man':
            if call.message.chat.type == 'private':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=call.message.text, reply_markup=None)
                if check_sub_channel(bot.get_chat_member(chat_id='@hypewear22', user_id=call.message.chat.id)):
                    bot.send_message(call.message.chat.id, 'Вы не подписались на канал❌')
                    bot.send_message(call.message.chat.id,"Для просмотра товаров необходимо подписаться на канал\n@hypewear22 💬", reply_markup=subscribe_man)
                else:
                    bot.send_message(call.message.chat.id, 'Благодарим за подписку✅')
                    bot.send_message(call.message.chat.id, 'Выберите категорию: ', reply_markup=category)
                    male = 'муж'
                    bot.register_next_step_handler(call.message, user_chois, male)
        if call.data == 'Chek_girl':
            if call.message.chat.type == 'private':
                if check_sub_channel(bot.get_chat_member(chat_id='@yummyAliExpress', user_id=call.message.chat.id)):
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=call.message.text, reply_markup=None)
                    bot.send_message(call.message.chat.id, 'Вы не подписались на канал❌')
                    bot.send_message(call.message.chat.id,"Для просмотра товаров необходимо подписаться на канал\n@yummyAliExpress 💬", reply_markup=subscribe_girl)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=call.message.text, reply_markup=None)
                    bot.send_message(call.message.chat.id, 'Благодарим за подписку✅')
                    bot.send_message(call.message.chat.id, 'Выберите категорию: ', reply_markup=category_girls)
                    male = 'жен'
                    bot.register_next_step_handler(call.message, user_chois, male)

    def girl_boy_step(message):
        if message.text == 'Мужской':
            if message.chat.type == 'private':
                if check_sub_channel(bot.get_chat_member(chat_id='@hypewear22', user_id=message.chat.id)):
                    bot.send_message(message.chat.id,"Для просмотра товаров необходимо подписаться на канал👇", reply_markup=types.ReplyKeyboardRemove())
                    bot.send_message(message.chat.id,"@hypewear22 💬", reply_markup=subscribe_man)
                else:
                    bot.send_message(message.chat.id, 'Выберите категорию: ', reply_markup=category)
                    male = 'муж'
                    bot.register_next_step_handler(message, user_chois, male)
        elif message.text == 'Женский':
            if message.chat.type == 'private':
                if check_sub_channel(bot.get_chat_member(chat_id='@yummyAliExpress', user_id=message.chat.id)):
                    bot.send_message(message.chat.id,"Для просмотра товаров необходимо подписаться на канал👇", reply_markup=types.ReplyKeyboardRemove())
                    bot.send_message(message.chat.id,"@yummyAliExpress 💬", reply_markup=subscribe_girl)
                else:
                    bot.send_message(message.chat.id, 'Выберите категорию: ', reply_markup=category_girls)
                    male = 'жен'
                    bot.register_next_step_handler(message, user_chois, male)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=user_main)
        else:
            bot.send_message(message.chat.id, 'Нажмите пожалуйста кнопку')
            bot.register_next_step_handler(message, girl_boy_step)

    def user_chois(message, male):
        if male == 'муж':
            if message.chat.type == 'private':
                if check_sub_channel(bot.get_chat_member(chat_id='@hypewear22', user_id=message.chat.id)):
                    bot.send_message(message.chat.id,"Для просмотра товаров необходимо подписаться на канал👇", reply_markup=types.ReplyKeyboardRemove())
                    bot.send_message(message.chat.id,"@hypewear22 💬", reply_markup=subscribe_man)
                else:
                    category = message.text.lower()
                    prise = 'Смотреть все'
                    if category == "бижутерия" or category == "бомберы" or category == "кепки" or category == "шапки" or category == "аниме"  or category == "шорты" or category == "очки" or category == "сумки" or category == "рубашки" or category == "обувь" or category == "ночники" or category == "пижамы" or category == "колготки" or category == "спорттовары" or category == "чокеры" or category == "рюкзаки" or category == "топы" or category == "платья" or category == "юбки" or category == "кардиганы" or category == "перчатки" or category == "свитера" or category == "куртки" or category == "ветровки" or category == "пальто" or category == "шарфы" or category == "1000мелочей":
                        user_prise(message, category, male, prise)
                    elif category == "футболки":
                        bot.send_message(message.chat.id, 'Выберите ценовую категорию', reply_markup=prise_fytbolka)
                        bot.register_next_step_handler(message, user_prise, category, male, prise)
                    elif category == "кофты":
                        bot.send_message(message.chat.id, 'Выберите ценовую категорию', reply_markup=prise_koft)
                        bot.register_next_step_handler(message, user_prise, category, male, prise)
                    elif category == "штаны":
                        bot.send_message(message.chat.id, 'Выберите ценовую категорию', reply_markup=prise_shtani)
                        bot.register_next_step_handler(message, user_prise, category, male, prise)
                    elif category == "вернуться в меню":
                        bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=user_main)
                    else:
                        bot.send_message(message.chat.id, 'Неверно выбрана категория')
                        bot.register_next_step_handler(message, user_chois, male)
        elif male == 'жен':
            if message.chat.type == 'private':
                if check_sub_channel(bot.get_chat_member(chat_id='@yummyAliExpress', user_id=message.chat.id)):
                    bot.send_message(message.chat.id,"Для просмотра товаров необходимо подписаться на канал👇", reply_markup=types.ReplyKeyboardRemove())
                    bot.send_message(message.chat.id,"@yummyAliExpress 💬", reply_markup=subscribe_girl)
                else:
                    category = message.text.lower()
                    prise = 'Смотреть все'
                    if category == "бижутерия" or category == "бомберы" or category == "кепки" or category == "шапки" or category == "аниме"  or category == "шорты" or category == "очки" or category == "сумки" or category == "рубашки" or category == "обувь" or category == "ночники" or category == "пижамы" or category == "колготки" or category == "спорттовары" or category == "чокеры" or category == "рюкзаки" or category == "топы" or category == "платья" or category == "юбки" or category == "кардиганы" or category == "перчатки" or category == "свитера" or category == "куртки" or category == "ветровки" or category == "пальто" or category == "шарфы" or category == "1000мелочей":
                        user_prise(message, category, male, prise)
                    elif category == "футболки":
                        bot.send_message(message.chat.id, 'Выберите ценовую категорию', reply_markup=prise_fytbolka)
                        bot.register_next_step_handler(message, user_prise, category, male, prise)
                    elif category == "кофты":
                        bot.send_message(message.chat.id, 'Выберите ценовую категорию', reply_markup=prise_koft)
                        bot.register_next_step_handler(message, user_prise, category, male, prise)
                    elif category == "штаны":
                        bot.send_message(message.chat.id, 'Выберите ценовую категорию', reply_markup=prise_shtani)
                        bot.register_next_step_handler(message, user_prise, category, male, prise)
                    elif category == "вернуться в меню":
                        bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=user_main)
                    else:
                        bot.send_message(message.chat.id, 'Неверно выбрана категория')
                        bot.register_next_step_handler(message, user_chois, male)

    def user_prise(message, category, male, prise):
        if male == 'муж':
            if message.chat.type == 'private':
                if check_sub_channel(bot.get_chat_member(chat_id='@hypewear22', user_id=message.chat.id)):
                    bot.send_message(message.chat.id,"Для просмотра товаров необходимо подписаться на канал👇", reply_markup=types.ReplyKeyboardRemove())
                    bot.send_message(message.chat.id,"@hypewear22 💬", reply_markup=subscribe_man)
                else:
                    if message.text == 'Вернуться в меню':
                        bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=user_main)
                    else:
                        con_user = sqlite3.connect('database.db', check_same_thread=False)
                        cursor_user = con_user.cursor()
                        tovar = 0
                        reiting = '0'
                        if category == message.text.lower() or message.text == 'Смотреть все':
                            tovar = cursor_user.execute("select * from `tovar` WHERE `category` = ? AND `male` = ? AND `reiting` != ?", (category, male, reiting)).fetchall()    
                        else:
                            prise = str(message.text)
                            prise = prise.replace(",", '.')
                            check_prise = "+" in prise
                            try:
                                if check_prise == True:
                                    prise_min = float(prise.replace("+", ''))
                                    prise_max = 1000000
                                elif check_prise == False:
                                    prise_min = float(prise.split('-')[0])
                                    prise_max = float(prise.split('-')[-1])
                                tovar = cursor_user.execute("select * from `tovar` WHERE `cost_for_user` >= ? AND `cost_for_user` <= ? AND `category` = ? AND `male` = ? AND `reiting` != ?", (prise_min, prise_max, category, male, reiting)).fetchall()
                            except:
                                bot.send_message(message.chat.id, 'попробуйте указать ценовой диапазон ещё раз')
                                bot.register_next_step_handler(message, user_prise, category, male)
                        con_user.close()
                        try:
                            item_for_send = tovar[random.randrange(0, len(tovar))]
                            bot.send_message(message.chat.id, 'Товары найденные по вашему запросу', reply_markup=markup_watch)
                            bot.send_photo(message.chat.id, item_for_send[5], caption=f'💸{item_for_send[1]}\n🌟{item_for_send[2]}/5\n🛒{item_for_send[3]}\n~ {item_for_send[4]}')
                            bot.register_next_step_handler(message, watch, tovar, male)
                        except:
                            bot.send_message(message.chat.id, 'по вашему запросу ничего не найдено', reply_markup=user_main)
        elif male == 'жен':
            if message.chat.type == 'private':
                if check_sub_channel(bot.get_chat_member(chat_id='@yummyAliExpress', user_id=message.chat.id)):
                    bot.send_message(message.chat.id,"Для просмотра товаров необходимо подписаться на канал👇", reply_markup=types.ReplyKeyboardRemove())
                    bot.send_message(message.chat.id,"@yummyAliExpress 💬", reply_markup=subscribe_girl)
                else:
                    if message.text == 'Вернуться в меню':
                        bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=user_main)
                    else:
                        con_user = sqlite3.connect('database.db', check_same_thread=False)
                        cursor_user = con_user.cursor()
                        tovar = 0
                        reiting = '0'
                        if prise == 'Смотреть все':
                            tovar = cursor_user.execute("select * from `tovar` WHERE `category` = ? AND `male` = ? AND `reiting` != ?", (category, male, reiting)).fetchall()    
                        elif prise != 'Смотреть все':
                            prise = str(message.text)
                            prise = prise.replace(",", '.')
                            check_prise = "+" in prise
                            try:
                                if check_prise == True:
                                    prise_min = float(prise.replace("+", ''))
                                    prise_max = 1000000
                                elif check_prise == False:
                                    prise_min = float(prise.split('-')[0])
                                    prise_max = float(prise.split('-')[-1])
                                tovar = cursor_user.execute("select * from `tovar` WHERE `cost_for_user` >= ? AND `cost_for_user` <= ? AND `category` = ? AND `male` = ? AND `reiting` != ?", (prise_min, prise_max, category, male, reiting)).fetchall()
                            except:
                                bot.send_message(message.chat.id, 'попробуйте указать ценовой диапазон ещё раз')
                                bot.register_next_step_handler(message, user_prise, category, male)
                        con_user.close()
                        try:
                            item_for_send = tovar[random.randrange(0, len(tovar))]
                            bot.send_message(message.chat.id, 'Товары найденные по вашему запросу', reply_markup=markup_watch)
                            bot.send_photo(message.chat.id, item_for_send[5], caption=f'💸{item_for_send[1]}\n🌟{item_for_send[2]}/5\n🛒{item_for_send[3]}\n~ {item_for_send[4]}')
                            bot.register_next_step_handler(message, watch, tovar, male)
                        except:
                            bot.send_message(message.chat.id, 'по вашему запросу ничего не найдено', reply_markup=user_main)

    def watch(message, tovar, male):
        if male == 'муж' and message.text != 'Вернуться в меню':
            if message.chat.type == 'private':
                if check_sub_channel(bot.get_chat_member(chat_id='@hypewear22', user_id=message.chat.id)):
                    bot.send_message(message.chat.id,"Для просмотра товаров необходимо подписаться на канал👇", reply_markup=types.ReplyKeyboardRemove())
                    bot.send_message(message.chat.id,"@hypewear22 💬", reply_markup=subscribe_man)
                else:
                    if message.text == 'Смотреть ещё':
                        item_for_send = tovar[random.randrange(0, len(tovar))]
                        bot.send_photo(message.chat.id, item_for_send[5], caption=f'💸{item_for_send[1]}\n🌟{item_for_send[2]}/5\n🛒{item_for_send[3]}\n~ {item_for_send[4]}')
                        bot.register_next_step_handler(message, watch, tovar, male)
                    else: 
                        bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку')
        elif male == 'жен' and message.text != 'Вернуться в меню':
            if message.chat.type == 'private':
                if check_sub_channel(bot.get_chat_member(chat_id='@yummyAliExpress', user_id=message.chat.id)):
                    bot.send_message(message.chat.id,"Для просмотра товаров необходимо подписаться на канал👇", reply_markup=types.ReplyKeyboardRemove())
                    bot.send_message(message.chat.id,"@yummyAliExpress 💬", reply_markup=subscribe_girl)
                else:
                    if message.text == 'Смотреть ещё':
                        item_for_send = tovar[random.randrange(0, len(tovar))]
                        bot.send_photo(message.chat.id, item_for_send[5], caption=f'💸{item_for_send[1]}\n🌟{item_for_send[2]}/5\n🛒{item_for_send[3]}\n~ {item_for_send[4]}')
                        bot.register_next_step_handler(message, watch, tovar, male)
                    else: 
                        bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку')
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'Добро пожаловать в главное меню', reply_markup=user_main)

    def add_tovar_girl_boy_step(message):
        if message.text == 'Мужской':
            bot.send_message(message.chat.id, 'Пришли ссылку на товар: ', reply_markup=markup_back)
            male = 'муж'
            bot.register_next_step_handler(message, add_tovar_base, male)
        elif message.text == 'Женский':
            bot.send_message(message.chat.id, 'Пришли ссылку на товар: ', reply_markup=markup_back)
            male = 'жен'
            bot.register_next_step_handler(message, add_tovar_base, male)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=admin)
        else:
            bot.send_message(message.chat.id, 'Нажмите пожалуйста кнопку')
            bot.register_next_step_handler(message, add_tovar_girl_boy_step)

    def add_tovar_base(message, male):
        link = message.text
        if link != 'Вернуться в меню':
            check_link = "http://al" in link
            if check_link == True:
                if male == 'муж':
                    bot.send_message(message.chat.id, 'Выберите категорию: ', reply_markup=category)
                elif male == 'жен':
                    bot.send_message(message.chat.id, 'Выберите категорию: ', reply_markup=category_girls)
                bot.register_next_step_handler(message, add_tovar_base_category, link, male)
            elif check_link == False:
                bot.send_message(message.chat.id, 'Попробуйте прислать ссылку ещё раз', reply_markup=markup_back)
                bot.register_next_step_handler(message, add_tovar_base, male)
        elif link == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=admin)

    def add_tovar_base_category(message, link, male):
        category = message.text.lower()
        if category != "вернуться в меню" and (category == "бижутерия" or category == "бомберы" or category == "аниме" or category == "кепки" or category == "шапки" or category == "шорты" or category == "очки" or category == "сумки" or category == "рубашки" or category == "обувь" or category == "ночники" or category == "свитера" or category == "куртки" or category == "ветровки" or category == "пальто" or category == "шарфы" or category == "1000мелочей" or category == "штаны" or category == "кофты" or category == "футболки" or category == "бижутерия" or category == "свитера" or category == "кепки" or category == "шапки" or category == "аниме" or category == "очки" or category == "сумки" or category == "рубашки" or category == "обувь" or category == "ночники" or category == "куртки" or category == "перчатки" or category == "кардиганы" or category == "пижамы" or category == "рюкзаки" or category == "топы" or category == "платья" or category == "юбки" or category == "колготки" or category == "спорттовары" or category == "чокеры" or category == "1000мелочей" or category == "кофты" or category == "футболки"):
            conn_add_tovar = sqlite3.connect('database.db', check_same_thread=False)
            cursor_add_tovar = conn_add_tovar.cursor()
            cursor_add_tovar.execute('INSERT INTO tovar (category, cost_for_update, reiting, sold, link, photo_1, cost_for_user, male) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (category, '0', '0', '0', link, '0', 1, male))
            conn_add_tovar.commit()
            conn_add_tovar.close()
            bot.send_message(message.chat.id, 'Товар успешно добавлен', reply_markup=admin)
        elif category == "вернуться в меню":
            bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=admin)
        else:
            bot.send_message(message.chat.id, 'Неверно выбрана категория', reply_markup=admin)

    def database(message):
        conn_add_user = sqlite3.connect('database.db', check_same_thread=False)
        cursor_add_user = conn_add_user.cursor()
        info = cursor_add_user.execute('SELECT * FROM users WHERE user_id=?', (message.from_user.id, )) 
        if info.fetchone() is None: 
            dt = datetime.datetime.now() 
            dt = dt.strftime(dt.strftime("%d-%m-%Y"))
            cursor_add_user.execute('INSERT INTO users (user_id, user_name, user_surname, username, datetime) VALUES (?, ?, ?, ?, ?)', (message.from_user.id , message.from_user.first_name, message.from_user.last_name, message.from_user.username, dt))
            conn_add_user.commit()
        conn_add_user.close()
    
    def chek_alik(message): 
        con_chek_alik_prefer = sqlite3.connect('database.db', check_same_thread=False)
        cursor_chek_alik_prefer = con_chek_alik_prefer.cursor()
        check_info = cursor_chek_alik_prefer.execute("select * from `tovar`").fetchall()
        con_chek_alik_prefer.close()
        driver = uc.Chrome()
        kapcha(message, check_info, driver)
            
    def kapcha(message, check_info, driver):
        try:
            for row in check_info:
                link = row[4]
                category = row[0]
                male = row[7]
                if message != 0:
                    back = message.text
                else:
                    back = 0
                if back != 'Вернуться в меню':
                    con_kapcha = sqlite3.connect('database.db', check_same_thread=False)
                    cursor_kapcha = con_kapcha.cursor()
                    driver.get(link)
                    time.sleep(settings.time)
                    response = driver.page_source.encode('utf-8')
                    soup = BeautifulSoup(response, 'lxml')
                    tovar_actual = soup.find(text="К сожалению, этот товар уже недоступен!")
                    page_actual = soup.find(text="Ой, страница не найдена :-(")
                    if tovar_actual == 'К сожалению, этот товар уже недоступен!':
                        cursor_kapcha.execute("DELETE FROM `tovar` WHERE `link` = ?", (link,))
                        con_kapcha.commit()
                    elif page_actual == 'Ой, страница не найдена :-(':
                        cursor_kapcha.execute("DELETE FROM `tovar` WHERE `link` = ?", (link,))
                        con_kapcha.commit()
                    else:
                        reiting = soup.find('span', class_='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1').text.replace("руб.", '')
                        sold = soup.find('span', class_='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Label__label__1n9sab ali-kit_Label__size-s__1n9sab').text
                        try:
                            cost = soup.find('span', class_='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 price ali-kit_Price__size-xl__12ybyf Product_Price__current__1uqb8 product-price-current').text.replace("руб.", '').replace(",", '.').replace("\xa0", '').replace(" ", '')
                        except:
                            cost = soup.find('span', class_='Product_UniformBanner__uniformBannerBoxPrice__o5qwb').text.replace("руб.", '').replace(",", '.').replace("\xa0", '').replace(" ", '')
                        photo = soup.find_all('img', class_="ali-kit_Image__image__1jaqdj")
                        if  ".png" in photo[0]['src']:
                            photo_1 = photo[1]['src']
                        else:
                            photo_1 = photo[0]['src']
                        photo_1 = photo_1.replace("50x50", '').replace("100x100", '').replace("640x640", '')
                        prise_dostavka = soup.find('span', class_='freight-extra-info-detail').text.replace("руб.", '').replace(",", '.').replace("\xa0", '').replace(" ", '').replace("за", '')
                        cost_min = cost.split(' - ')[0]
                        cost_max = cost.split(' - ')[-1]
                        if cost_min == cost_max and prise_dostavka != 'Бесплатно':
                            cost = (f'{round(float(prise_dostavka) + float(cost_min), 2)}₽')
                            cost_for_user = round(float(prise_dostavka) + float(cost_min), 2)
                        elif cost_min != cost_max and prise_dostavka != 'Бесплатно':
                            cost = (f'{round(float(prise_dostavka) + float(cost_min), 2)}₽ - {round(float(prise_dostavka) + float(cost_max), 2)}₽')
                            cost_for_user = round(float(prise_dostavka) + float(cost_max), 2)
                        elif cost_min == cost_max and prise_dostavka == 'Бесплатно':
                            cost = (f'{round(float(cost_min), 2)}₽')
                            cost_for_user = round(float(cost_min), 2)
                        elif cost_min != cost_max and prise_dostavka == 'Бесплатно':
                            cost = (f'{round(float(cost_min), 2)}₽ - {round(float(cost_max), 2)}₽')
                            cost_for_user = round(float(cost_max), 2)
                        info = cursor_kapcha.execute('SELECT * FROM `tovar` WHERE  `cost_for_update` = ? AND `cost_for_user` = ? AND `sold` = ? AND `reiting` = ? AND `photo_1` = ?  AND `category` = ?  AND `male` = ?', (cost, cost_for_user, sold, reiting, photo_1, category, male)).fetchone()
                        try:
                            length = len(info)
                        except:
                            length = 0
                        if length == 16:
                            cursor_kapcha.execute("DELETE FROM `tovar` WHERE `link` = ?", (link,))
                            con_kapcha.commit()
                        else:
                            cursor_kapcha.execute("UPDATE `tovar` SET `cost_for_update` = ?, `cost_for_user` = ? , `sold` = ?, `reiting` = ?, `photo_1` = ? WHERE `link` = ?", (cost, cost_for_user, sold, reiting, photo_1, link))
                            con_kapcha.commit()
                        check_info.remove(row)
                    con_kapcha.close()
                else:
                    if message != 0:
                        bot.send_message(message.chat.id, 'Вы в начальном меню', reply_markup=admin)
                    elif message == 0:
                        bot.send_message(chat_id, 'Вы в начальном меню', reply_markup=admin)
            driver.quit()
            if message != 0:
                bot.send_message(message.chat.id, f'Таблица товаров обновлена')
            elif message == 0:
                bot.send_message(chat_id, 'Таблица товаров обновлена')
        except Exception:
            bot.send_message(chat_id, traceback.format_exc())
            if message != 0:
                bot.send_message(message.chat.id, f'Выполни капчу и напиши что-то мне', reply_markup=markup_back)
            elif message == 0:
                bot.send_message(chat_id, f'Выполни капчу и напиши что-то мне', reply_markup=markup_back)
            bot.register_next_step_handler(message, kapcha, check_info, driver)
            
    def rassilka_step(message):
        message_important = message
        bot.send_message(message.chat.id, 'Вы уверены что отправить?', reply_markup= markup_send)
        bot.register_next_step_handler(message, rassilka, message_important)
        
    def rassilka(message, message_important):
        if message.text == 'Отправить':
            try:
                conn_rassilka = sqlite3.connect('database.db', check_same_thread=False)
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
            except Exception:
                bot.send_message(chat_id, traceback.format_exc())
                bot.send_message(message.chat.id, 'произошла ошибка', reply_markup = admin)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup = admin)
        else:
            bot.send_message(message.chat.id, 'нажмите пожалуйста на кнопку')
            bot.register_next_step_handler(message, rassilka, message_important)

    def job():
        chek_alik(0)

    def target_time():
        schedule.every().day.at("00:00").do(job)
        while True:
            schedule.run_pending()
            time.sleep(5)

    thread_check_time = Thread(target=target_time)
    thread_check_time.start()

    bot.polling()

if __name__ == '__main__':
    while True:
        try:
            start_program()
        except Exception:
            print(traceback.format_exc())