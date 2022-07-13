import sqlite3
import telebot
from telebot import types
import traceback
import datetime
import time
import random
import requests
from bs4 import BeautifulSoup
import difflib
import schedule
from threading import Thread

user_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("новости")
item2 = types.KeyboardButton("матчи моей команды")
item3 = types.KeyboardButton("матчи")
item4 = types.KeyboardButton("Стастистика игроков")
item5 = types.KeyboardButton("Трансферы") 
item6 = types.KeyboardButton("Бомбардиры") 
item7 = types.KeyboardButton("Слухи о трансферах") 
user_main.add(item1, item2, item3, item4, item5, item6, item7)

admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("сделать рассылку")
item2 = types.KeyboardButton("перейти в пользовательскую версию")
admin.add(item1, item2)

znakomstvo = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Познакомиться")
item2 = types.KeyboardButton("о боте")
znakomstvo.add(item1, item2)

club_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Chelsea")
item2 = types.KeyboardButton("Villarreal")
item3 = types.KeyboardButton("Atletico Madrid")
item4 = types.KeyboardButton("Real Madrid")
item5 = types.KeyboardButton("Barcelona")
item6 = types.KeyboardButton("Sevilla")
item7 = types.KeyboardButton("Manchester City")
item8 = types.KeyboardButton("Manchester United")
item9 = types.KeyboardButton("Liverpool")
item10 = types.KeyboardButton("Bayern Munich")
item11 = types.KeyboardButton("RB Leipzig")
item12 = types.KeyboardButton("Bo Dortmund")
item13 = types.KeyboardButton("VfL Wolfsburg")
item14 = types.KeyboardButton("Inter Milan")
item15 = types.KeyboardButton("Milan")
item16 = types.KeyboardButton("Atalanta")
item17 = types.KeyboardButton("Juventus")
item18 = types.KeyboardButton("Lille")
item19 = types.KeyboardButton("Paris Saint-Germain")
item20 = types.KeyboardButton("Sporting CP")
item21 = types.KeyboardButton("Porto")
item22 = types.KeyboardButton("Zenit Saint Petersburg")
item23 = types.KeyboardButton("Club Brugge")
item24 = types.KeyboardButton("Dynamo Kyiv")
item25 = types.KeyboardButton("Ajax")
item26 = types.KeyboardButton("Besiktas")
club_key.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26)

numb = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("1")
item2 = types.KeyboardButton("2")
item3 = types.KeyboardButton("3")
item4 = types.KeyboardButton("4")
item5 = types.KeyboardButton("5")
item6 = types.KeyboardButton("6")
item7 = types.KeyboardButton("7")
item8 = types.KeyboardButton("8")
item9 = types.KeyboardButton("9")
item10 = types.KeyboardButton("10")
numb.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

yes_no = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Да")
item2 = types.KeyboardButton("Нет")
yes_no.add(item1, item2)

forgot = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Помнить меня")
item2 = types.KeyboardButton("Забыть меня")
forgot.add(item1, item2)

clock = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Узнать время")
item2 = types.KeyboardButton("Поставить будильник")
clock.add(item1, item2)

maybe_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Да")
item2 = types.KeyboardButton("Нет")
maybe_key.add(item1, item2)


result_of_leage = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Расписание")
item2 = types.KeyboardButton("Результаты")
result_of_leage.add(item1, item2)

leages = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Лига чемпионов")
item2 = types.KeyboardButton("Лига европпы")
item3 = types.KeyboardButton("Премьер лига")
item4 = types.KeyboardButton("Ла лига")
item5 = types.KeyboardButton("Серия А")
leages.add(item1, item2, item3, item4, item5)

with  open(f'photo/lisui_hren.jpg', 'rb') as image_file:
    photo_hren = image_file.read()
with  open(f'photo/macho.jpg', 'rb') as image_file:
    photo_macho = image_file.read()
with  open(f'photo/ya_tebya_vishu.jpg', 'rb') as image_file:
    photo_vishu = image_file.read()
sticker_amazing = 'CAACAgIAAxkBAANiYp30O-zgWy0Oz6Rd8pc491C8z14AAh8AAyShGA73zE1cexljyyQE'
sticker_happy = 'CAACAgIAAxkBAAN_Yp31pFdafimINh64Y-U-XS0bxHUAAi4AAyShGA4LYiBWTaZQuiQE'
sticker_interes = 'CAACAgIAAxkBAAOBYp31qiORAwpjJLbIGC-uj0rpsQgAAikAAyShGA4gRhChGOHkrSQE'

def start_program():
    chat_id_Maksim = 5209538522
    token = 'TOKEN'
    bot = telebot.TeleBot(token)
    
    Kimberg = sqlite3.connect('Kimberg_base.db', check_same_thread=False)
    cursor = Kimberg.cursor()

    list_players = []
    type (list_players)

    @bot.message_handler(commands=['start'])    
    def welcome(message):
        database(message)
        if " " in message.text:
            referrer_candidate = message.text.split()[1]
            if referrer_candidate == 'Admin' and message.chat.id == chat_id_Maksim:
                bot.send_message(message.chat.id, 'Приветствую вас о мой господин', reply_markup=admin)
            else:
                bot.send_message(message.chat.id, 'Спасибо, что воспользовались рекомандацией @'+ referrer_candidate)
        info = cursor.execute('SELECT * FROM category_Kimberg WHERE user_id=?', (message.chat.id, )) 
        if info.fetchone() is None:
            bot.send_sticker(message.chat.id, sticker_amazing)
            bot.send_message(message.chat.id, 'Опа кто зашёл')
            bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>🤖, и мы будем вместе следить за успехами Juventus.\n А теперь мне не терпиться с тобой познакомиться.".format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Я так рад с тобой познакомиться.\n Как к тебе обращаться?')
            bot.register_next_step_handler(message, znakomstvo_name)
        else:
            info_user = cursor.execute("select * from `category_Kimberg` WHERE `user_id` = ?", (message.chat.id, ))
            info_user = info_user.fetchall()
            for row in info_user:
                bot.send_photo(message.chat.id, photo_vishu, caption=f'Ты меня развести пытался? я всё знаю о тебе\n Ты - {row[2]}\n Болеешь за - {row[3]}')
                bot.send_message(message.chat.id, 'Или ты хочешь чтобы я делал вид что я тебя не знаю?', reply_markup=forgot)
                bot.register_next_step_handler(message, forgot_user)

    @bot.message_handler(commands=['help']) 
    def help(message):
        bot.send_message(message.chat.id, "Я - <b>{1.first_name}</b>🤖, и бываю приставучим иногда тебя спасёт команда /skip, но когда это не тебе решать\n А теперь мне не терпиться с тобой познакомиться.".format(message.from_user, bot.get_me()),
            parse_mode='html')

    def forgot_user(message):
        if message.text == 'Помнить меня':
            bot.send_sticker(message.chat.id, sticker_happy)
            bot.send_message(message.chat.id, 'Другое дело удачи в пользовании', reply_markup=user_main)
        elif message.text == 'Забыть меня':
            bot.send_photo(message.chat.id, photo_hren,caption='а хрена тебе лысого', reply_markup=types.ReplyKeyboardRemove())
            time.sleep(10)
            bot.send_message(message.chat.id, 'Ладно я сегодня игривый так уж и быть сделаю вид, что не помню кто ты. Как тебя звать?')
            bot.register_next_step_handler(message, znakomstvo_name)
        else:
            bot.send_message(message.chat.id, 'Слабо по кнопке попасть?')

    def znakomstvo_name(message):
        name = message.text
        if name == 'бог' or name == 'господин' or name == 'гений' or name == 'царь':
            bot.send_message(message.chat.id, 'Выбери что-то по проще')
            bot.send_photo(message.chat.id, photo_hren, caption='лови дядьку')
            bot.register_next_step_handler(message, znakomstvo_name)
        else:
            bot.send_message(message.chat.id, 'За какой клуб болеешь?', reply_markup=club_key)
            bot.register_next_step_handler(message, znakomstvo_favorite_club, name)

    def znakomstvo_favorite_club(message, name):
        club = message.text
        if club == 'Chelsea' or club == 'Villarreal' or club == 'Atletico Madrid' or club == 'Real Madrid' or club == 'Barcelona' or club == 'Sevilla' or club == 'Manchester City' or club == 'Bayern Munich' or club == 'RB Leipzig' or club == 'Liverpool' or club == 'Bo Dortmund' or club == 'VfL Wolfsburg' or club == 'Inter Milan' or club == 'Milan' or club == 'Atalanta' or club == 'Lille' or club == 'Paris Saint-Germain' or club == 'Sporting CP' or club == 'Porto' or club == 'Zenit Saint Petersburg' or club == 'Club Brugge' or club == 'Dynamo Kyiv' or club == 'Ajax' or club == 'Besiktas' or club == 'Manchester United':
            caption = 'Хорошая команда но теперь ты болеешь за Juventus\n Теперь самый важный вопрос как тебе мужик на фотке?'
            add_base_inform(message, name, club)
            bot.send_photo(message.chat.id, photo_macho, caption=caption, reply_markup=numb)
            bot.register_next_step_handler(message, znakomstvo_yan, name, club)
        elif club == 'Juventus':
            caption = 'Черно-белые? отличный выбор.\n Теперь самый важный вопрос как тебе мужик на фотке?'
            add_base_inform(message, name, club)
            bot.send_photo(message.chat.id, photo_macho, caption=caption, reply_markup=numb)
            bot.register_next_step_handler(message, znakomstvo_yan, name, club)
        else:
            maybe = difflib.get_close_matches(club, ['Chelsea', 'Villarreal', 'Atletico Madrid', 'Real Madrid', 'Barcelona', 'Sevilla', 'Manchester City', 'Bayern Munich', 'RB Leipzig', 'Liverpool', 'Bo Dortmund', 'VfL Wolfsburg', 'Inter Milan', 'Milan', 'Atalanta', 'Lille', 'Paris Saint-Germain', 'Sporting CP', 'Porto', 'Zenit Saint Petersburg', 'Club Brugge', 'Dynamo Kyiv', 'Ajax', 'Besiktas', 'Manchester United'])
            try:
                maybe = maybe[0]
                bot.send_message(message.chat.id, f'Возможно вы имели в виду - {maybe}?', reply_markup=maybe_key)
                bot.register_next_step_handler(message, maybe_func, name, club, maybe)
            except:
                bot.send_message(message.chat.id, 'Пффф тяжелый случай')
                bot.register_next_step_handler(message, znakomstvo_favorite_club, name)

    def maybe_func(message, name, club, maybe):
        if message.text == 'Да':
            caption = 'Да я просто ванга\n Теперь самый важный вопрос как тебе мужик на фотке?'
            add_base_inform(message, name, maybe)
            bot.send_photo(message.chat.id, photo_macho, caption=caption, reply_markup=numb)
            bot.register_next_step_handler(message, znakomstvo_yan, name, maybe)
        elif message.text == 'Нет':
            bot.send_message(message.chat.id, 'Тогда укажи название команды, но теперь нормально', reply_markup=club_key)
            bot.register_next_step_handler(message, znakomstvo_favorite_club, name)
        else:
            bot.send_message(message.chat.id, f'Щас бы в 2к22 по кнопке не попасть')
            bot.register_next_step_handler(message, maybe_func, name, club, maybe)

    def znakomstvo_yan(message, name, club):
        if message.text == '10':
            bot.send_message(message.chat.id, 'а мы с тобой во многом солидарны\n Продолжим знакомство?', reply_markup=yes_no)
            bot.register_next_step_handler(message, znakomstvo_yes_no, name, club)
        elif message.text == '/skip':
            bot.send_message(message.chat.id, 'А ты хитёр, ладно держи свои кнопки', reply_markup=user_main)
        else:
            bot.send_message(message.chat.id, 'Чот не заметил, чтобы ты нажал кнопку')
            bot.register_next_step_handler(message, znakomstvo_yan, name, club)

    def znakomstvo_yes_no(message, name, club):
        if message.text == 'Да':
            bot.send_sticker(message.chat.id, sticker_happy)
            bot.send_message(message.chat.id, 'оо как приятно', reply_markup=None)
            bot.send_message(message.chat.id, f'Ладно на этом всё ты в начальном меню\n сегодня я о тебе узнал что тебя зовут - {name}\n ты болеешь за - {club}', reply_markup=user_main)
        elif message.text == 'Нет':
            bot.send_message(message.chat.id, 'ха ну и надейся дальше что от тебя что-то зависит')
            bot.register_next_step_handler(message, znakomstvo_yes_no, name, club)
        elif message.text == '/skip':
            bot.send_message(message.chat.id, 'А ты хитёр, ладно держи свои кнопки', reply_markup=user_main)
        else:
            bot.send_message(message.chat.id, 'Слабо по кнопке попасть?')

    def add_base_inform(message, name, club):
        info = cursor.execute('SELECT * FROM category_Kimberg WHERE user_id=?', (message.chat.id, )) 
        if info.fetchone() is None:
            cursor.execute('INSERT INTO category_Kimberg (user_id, name, favorite_team) VALUES (?, ?, ?)', (message.chat.id, name, club))
            Kimberg.commit()
        else:
            cursor.execute("UPDATE `category_Kimberg` SET `name` = ? WHERE `user_id` = ?", (name, message.chat.id))
            Kimberg.commit()
            cursor.execute("UPDATE `category_Kimberg` SET `favorite_team`  = ? WHERE `user_id` = ?", (club, message.chat.id))
            Kimberg.commit()

    @bot.message_handler(content_types=["text"])
    def text(message): 
        if message.text == 'новости':
            numb = random.randint(1, 100)
            if numb == 10:
                bot.send_message(message.chat.id, 'Чот устал я от футбола я теперь будильник', reply_markup=clock)
                bot.register_next_step_handler(message, back)
            else:
                bot.send_message(message.chat.id, 'Выбери команду', reply_markup=club_key)
                bot.register_next_step_handler(message, news_chois_team)
        elif message.text == 'матчи моей команды':
            favorite_team = cursor.execute('SELECT `favorite_team` FROM category_Kimberg WHERE `user_id`=?', (message.chat.id,)) 
            favorite_team = favorite_team.fetchall()[0][0]
            team_link = favorite_team.replace("Atletico Madrid", 'atletico').replace("Real Madrid", 'real').replace("Bayern Munich", 'bayern').replace("Bo Dortmund", 'borussia').replace("VfL Wolfsburg", 'Wolfsburg').replace("Inter Milan", 'Inter').replace("Paris Saint-Germain", 'psg').replace("Sporting CP", 'Sporting').replace("Zenit Saint Petersburg", 'Zenit').replace("Club Brugge", 'brugge-fc').replace("Dynamo Kyiv", 'dynamo-kiev').replace("Ajax", 'ajax-fc').replace("Manchester United", 'mu').replace(" ", '-')
            link = f'https://www.sports.ru/{team_link}/calendar/'
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            match_of_favoriet_team = []
            table = soup.find('table', attrs={'class':'stat-table'})
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                match_of_favoriet_team.append([ele for ele in cols if ele]) 
            for match in match_of_favoriet_team:
                bot.send_message(message.chat.id, f'Дата - {match[0]}\nЛига - {match[1]}\n{favorite_team} - {match[2]}, {match[3]}')
        elif message.text == 'матчи':
            bot.send_message(message.chat.id, 'Выбери лигу', reply_markup=leages)
            bot.register_next_step_handler(message, leage_chois)
        elif message.text == 'Стастистика игроков':
            bot.send_message(message.chat.id, 'Выбери команду', reply_markup=club_key)
            bot.register_next_step_handler(message, statistika_chois)
        elif message.text == 'Трансферы':
            link = 'https://www.sports.ru/ucl/transfers/'
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            transfers = []
            table = soup.find('table', attrs={'class':'transfers-table js-active'})
            table_body = table.find('tbody', attrs={'class':'transfers-table__body'})
            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                transfers.append([ele for ele in cols if ele])   
            conter = 0
            while conter != 5:
                transfers[conter][2] = transfers[conter][2].replace("     ",' -> ')
                try:
                    transfers_srok = transfers[conter][4]
                except:
                    transfers_srok = '-'
                bot.send_message(message.chat.id, f'Новый трансфер:\nИмя-{transfers[conter][0]}, дата-{transfers[conter][1]}, Команды-{transfers[conter][2]}\n цена-{transfers[conter][3]}\n srok-{transfers_srok}')
                conter = conter + 1
        elif message.text == 'Бомбардиры':
            bot.send_message(message.chat.id, 'Выбери лигу', reply_markup=leages)
            bot.register_next_step_handler(message, bombardiers)
        elif message.text == '/skip':
            bot.send_message(message.chat.id, 'А ты хитёр, ладно держи свои кнопки', reply_markup=user_main)
        elif message.text == 'Слухи о трансферах':
            favorite_team = cursor.execute('SELECT `favorite_team` FROM category_Kimberg WHERE `user_id`=?', (message.chat.id,)) 
            favorite_team = favorite_team.fetchall()[0][0]
            team_link = favorite_team.replace("Atletico Madrid", 'atletico').replace("Real Madrid", 'real').replace("Bayern Munich", 'bayern').replace("Bo Dortmund", 'borussia').replace("VfL Wolfsburg", 'Wolfsburg').replace("Inter Milan", 'Inter').replace("Paris Saint-Germain", 'psg').replace("Sporting CP", 'Sporting').replace("Zenit Saint Petersburg", 'Zenit').replace("Club Brugge", 'brugge-fc').replace("Dynamo Kyiv", 'dynamo-kiev').replace("Ajax", 'ajax-fc').replace("Manchester United", 'mu').replace(" ", '-')
            link = f'https://www.sports.ru/{team_link}/'
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            transfers = soup.find('ul', class_='transfers__list list-reset')
            transfers = transfers.find_all('div', class_='transfers__description')
            for transfer in transfers:
                structer = transfer.find_all('div')
                pozition = structer[0].text
                clubs = structer[1].text
                link = structer[3].a['href']
                bot.send_message(message.chat.id, f'[{pozition}\n{clubs}]({link})', parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, 'ага щас разбежался я тебе отвечать')

    def bombardiers(message):
        if message.text == 'Лига чемпионов' or message.text == 'Лига европпы' or message.text == 'Премьер лига' or message.text == 'Ла лига' or message.text == 'Серия А':
            leage = message.text.replace("Лига чемпионов", 'Champions-League').replace("Лига европпы", 'Europa-League').replace("Премьер лига", 'England/Premier-League').replace("Ла лига", 'Spain/LaLiga').replace("Серия А", 'Italy/Serie-A')
            link = f'https://www.liveresult.ru/football/{leage}/statistics'
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            player_list = []
            player = soup.find('table', attrs={'class':'maintbl standings-table'})
            player = player.find('tbody')
            rows = player.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                player_list.append([ele for ele in cols if ele]) 
            bot.send_message(message.chat.id, f'{player_list[0][0]} - {player_list[0][2]}\nКлуб - {player_list[0][1]}\nГолы - {player_list[0][3]}\nПенальти - {player_list[0][4]}\nПередачи - {player_list[0][5]}')
            bot.send_message(message.chat.id, f'{player_list[1][0]} - {player_list[1][2]}\nКлуб - {player_list[1][1]}\nГолы - {player_list[1][3]}\nПенальти - {player_list[1][4]}\nПередачи - {player_list[1][5]}')
            bot.send_message(message.chat.id, f'{player_list[2][0]} - {player_list[2][2]}\nКлуб - {player_list[2][1]}\nГолы - {player_list[2][3]}\nПенальти - {player_list[2][4]}\nПередачи - {player_list[2][5]}')
            bot.send_message(message.chat.id, f'{player_list[3][0]} - {player_list[3][2]}\nКлуб - {player_list[3][1]}\nГолы - {player_list[3][3]}\nПенальти - {player_list[3][4]}\nПередачи - {player_list[3][5]}')
            bot.send_message(message.chat.id, f'{player_list[4][0]} - {player_list[4][2]}\nКлуб - {player_list[4][1]}\nГолы - {player_list[4][3]}\nПенальти - {player_list[4][4]}\nПередачи - {player_list[4][5]}')

    def news_chois_team(message):
        club = message.text
        if club == 'Chelsea' or club == 'Villarreal' or club == 'Atletico Madrid' or club == 'Real Madrid' or club == 'Barcelona' or club == 'Sevilla' or club == 'Manchester City' or club == 'Bayern Munich' or club == 'RB Leipzig' or club == 'Liverpool' or club == 'Bo Dortmund' or club == 'VfL Wolfsburg' or club == 'Inter Milan' or club == 'Milan' or club == 'Atalanta' or club == 'Lille' or club == 'Paris Saint-Germain' or club == 'Sporting CP' or club == 'Porto' or club == 'Zenit Saint Petersburg' or club == 'Club Brugge' or club == 'Dynamo Kyiv' or club == 'Ajax' or club == 'Besiktas' or club == 'Manchester United' or club == 'Juventus':
            club = club.replace("Atletico Madrid", 'atletico').replace("Real Madrid", 'real').replace("Bayern Munich", 'bayern').replace("Bo Dortmund", 'borussia').replace("VfL Wolfsburg", 'Wolfsburg').replace("Inter Milan", 'Inter').replace("Paris Saint-Germain", 'psg').replace("Sporting CP", 'Sporting').replace("Zenit Saint Petersburg", 'Zenit').replace("Club Brugge", 'brugge-fc').replace("Dynamo Kyiv", 'dynamo-kiev').replace("Ajax", 'ajax-fc').replace("Manchester United", 'mu').replace(" ", '-')
            link = f'https://www.sports.ru/{club}/'
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            newses = soup.find('div', class_='newsline')
            newses = newses.find_all('h2', class_='titleH2')
            for news in newses:
                news = news.a
                link = news['href']
                bot.send_message(message.chat.id, f'[{news.text}]({link})', parse_mode='Markdown', reply_markup=user_main)
        else:    
            bot.send_message(message.chat.id, 'Такой команды нет')
            bot.register_next_step_handler(message, news_chois_team)

    def back(message):
        bot.send_message(message.chat.id, 'ладно я пошутил держи свои кнопки обратно', reply_markup=user_main)

    def leage_chois(message):
        if message.text == 'Лига чемпионов' or message.text == 'Лига европпы' or message.text == 'Премьер лига' or message.text == 'Ла лига' or message.text == 'Серия А':
            leage = message.text.replace("Лига чемпионов", 'ucl').replace("Лига европпы", 'liga-europa').replace("Премьер лига", 'epl').replace("Ла лига", 'la-liga').replace("Серия А", 'seria-a')
            link = f'https://www.sports.ru/{leage}/calendar/'
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            match_list = []
            info = soup.find('div', attrs={'class':'mainPart columns-layout__main js-active'})
            info = info.find_all('table')
            for inf in info:
                rows = inf.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    match_list.append([ele for ele in cols if ele]) 
            for match in match_list:
                if match[2] == '- : -':
                    bot.send_message(message.chat.id, f'Дата - {match[0]}, {match[1]} - {match[3]}', reply_markup=user_main)

    def statistika_chois(message):
        club = message.text
        if club == 'Chelsea' or club == 'Villarreal' or club == 'Atletico Madrid' or club == 'Real Madrid' or club == 'Barcelona' or club == 'Sevilla' or club == 'Manchester City' or club == 'Bayern Munich' or club == 'RB Leipzig' or club == 'Liverpool' or club == 'Bo Dortmund' or club == 'VfL Wolfsburg' or club == 'Inter Milan' or club == 'Milan' or club == 'Atalanta' or club == 'Lille' or club == 'Paris Saint-Germain' or club == 'Sporting CP' or club == 'Porto' or club == 'Zenit Saint Petersburg' or club == 'Club Brugge' or club == 'Dynamo Kyiv' or club == 'Ajax' or club == 'Besiktas' or club == 'Manchester United' or club == 'Juventus':
            club = club.replace("Atletico Madrid", 'atletico').replace("Real Madrid", 'real').replace("Bayern Munich", 'bayern').replace("Bo Dortmund", 'borussia').replace("VfL Wolfsburg", 'Wolfsburg').replace("Inter Milan", 'Inter').replace("Paris Saint-Germain", 'psg').replace("Sporting CP", 'Sporting').replace("Zenit Saint Petersburg", 'Zenit').replace("Club Brugge", 'brugge-fc').replace("Dynamo Kyiv", 'dynamo-kiev').replace("Ajax", 'ajax-fc').replace("Manchester United", 'mu').replace(" ", '-')
            statistika_player(message, club)
        else:
            bot.send_message(message.chat.id, 'Такой команды нет')
            bot.register_next_step_handler(message, statistika_chois)

    def statistika_player(message, club):
            link = f'https://www.sports.ru/{club}/stat/2021-2022/'  #поставить текущий сезон
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            field = soup.find('table', class_='stat-table sortable-table js-active')
            names = field.find_all('a', class_='name')
            players_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
            players_fieald = {}
            for name in names:
                item = types.KeyboardButton(name.text)
                players_key.add(item)
                players_fieald[name.text.replace(" ", '')] = name['href']
            vratari = soup.find('table', class_='stat-table js-active')
            names = vratari.find_all('a', class_='name')
            players_vratari = {}
            for name in names:
                item = types.KeyboardButton(name.text)
                players_key.add(item)
                players_vratari[name.text.replace(" ", '')] = name['href']
            bot.send_message(message.chat.id, 'Выберите игрока', reply_markup=players_key)
            bot.register_next_step_handler(message, statistika_player_send, players_fieald, players_vratari)

    def statistika_player_send(message, players_fieald, players_vratari):
        try:
            link = players_fieald[message.text.replace(" ", '')]
            player = 'Полевой'
        except:
            link = players_vratari[message.text.replace(" ", '')]
            player = 'Вратарь'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'lxml')
        player_info = soup.find('table', class_='profile-table').text.strip().replace("\n\r\n", ' - ').replace("\r\n|\r\n", ' | ').replace("\r\n\n\n\n", '\n').replace("\n\n ", ' - ').replace("\r\n\n\n\n", '\n').replace("\n\n\xa0", ' - ').replace("\r\n - - ", '\n').replace("\r\n - ", ' - ')
        player_photo = soup.find('div', class_='img-box').img['src']
        bot.send_photo(message.chat.id, player_photo, caption=player_info)
        data_sezon = []
        data_carier = []
        table = soup.find('table', attrs={'class':'stat-table career'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data_sezon.append([ele for ele in cols if ele]) 
        table_body = table.find('tfoot')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data_carier.append([ele for ele in cols if ele])      
        seazon_yaer = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for row in data_sezon:
            if row[0] != 'Сезон':
                item = types.KeyboardButton(row[0])
                seazon_yaer.add(item)
        for row in data_carier:
            if row[0] != 'Сезон':
                bot.send_message(message.chat.id, f'Статистика за карьеру\n{row[0]}\nМатчей сыграно - ({row[1]}), среднее время на поле - ({row[8]}),\n Забил голов - ({row[2]}), Забил пенальти - ({row[3]}),\n Голевых передач - ({row[4]}), гол + пас - ({row[5]}),\n Желтых карточек - ({row[6]}), Красных карточек - ({row[7]})', reply_markup=user_main)        
        bot.send_message(message.chat.id, f'Выберите сезон', reply_markup=seazon_yaer)
        bot.register_next_step_handler(message, plaer_seazon, data_sezon, player)
      
    def plaer_seazon(message, data_sezon, player):
        for row in data_sezon:
            if row[0] == message.text:
                if player == 'Полевой':
                    bot.send_message(message.chat.id, f'Сезон - {row[0]}\nКоманда - {row[1]}\nТуринр - {row[2]}\n Матчей сыграно - ({row[3]}), среднее время на поле - ({row[10]}),\n Забил голов - ({row[4]}), Забил пенальти - ({row[5]}),\n Голевых передач - ({row[6]}), гол + пас - ({row[7]}),\n Желтых карточек - ({row[8]}), Красных карточек - ({row[9]})', reply_markup=user_main)
                elif player == 'Вратарь':
                     bot.send_message(message.chat.id, f'Сезон - {row[0]}\nКоманда - {row[1]}\nТуринр - {row[2]}\n Матчей сыграно - ({row[3]}), среднее время на поле - ({row[15]}),\n Забил голов - ({row[4]}), Забил пенальти - ({row[5]}),\n Голевых передач - ({row[6]}),\n Желтых карточек - ({row[7]}), Красных карточек - ({row[8]}), Пропущенных голов - ({row[9]}), Среднее число пропущенных голов - ({row[10]}), Сухих матчей - ({row[11]}), Выйгрышей - ({row[12]}), Ничьи - ({row[13]}), Поражений - ({row[14]})', reply_markup=user_main)

    def transfers_auto():
        link = 'https://www.sports.ru/ucl/transfers/'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'lxml')
        transfers = []
        table = soup.find('table', attrs={'class':'transfers-table js-active'})
        table_body = table.find('tbody', attrs={'class':'transfers-table__body'})
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            transfers.append([ele for ele in cols if ele])    
        for transfer in transfers:
            transfer[2] = transfer[2].replace("     ",' -> ')
            try:
                transfers_srok = transfer[4]
            except:
                transfers_srok = '-'
            info = cursor.execute('SELECT * FROM Transfers WHERE `name`=? AND `date`=? AND `teams`=? AND `prise`=? AND `srok`=?', (transfer[0], transfer[1], transfer[2], transfer[3], transfers_srok)) 
            if info.fetchone() is None:
                dt = datetime.datetime.now() 
                dt = dt.strftime(dt.strftime("Day: %d/%m/%Y  time: %H:%M:%S")) 
                cursor.execute('INSERT INTO Transfers (name, date, teams, prise, srok, datatime) VALUES (?, ?, ?, ?, ?, ?)', (transfer[0], transfer[1], transfer[2], transfer[3], transfers_srok, dt))
                Kimberg.commit()
                rassilka(transfer[0], transfer[1], transfer[2], transfer[3], transfers_srok)

    def rassilka(transfers_name, transfers_date, transfers_team, transfers_prise, transfers_srok):
        users = cursor.execute("select `user_id` from `category_Kimberg`")
        users = users.fetchall()
        numb = len(users)
        start_numb = 0
        while start_numb!=numb:
            try:
                bot.send_message(users[start_numb][0], f'Новый трансфер:\nИмя-{transfers_name}, дата-{transfers_date}, Команды-{transfers_team}\n цена-{transfers_prise}\n srok-{transfers_srok}')
            except:
                bot.send_message(chat_id_Maksim, f'Добавил в чс - {users[start_numb][0]}')
            start_numb = start_numb + 1

    @bot.message_handler(content_types=["sticker"])
    def sticker(message):
        file_id = message.sticker.file_id
        bot.send_message(message.chat.id, 'Отправил стикер молодец, мне то с ним что делать? ну держи обратно')
        bot.send_sticker(message.chat.id, file_id)
    
    @bot.message_handler(content_types=["voice"])
    def voice(message):
        file_id = message.voice.file_id
        bot.send_message(message.chat.id, 'А ну я прям в курсе, что делать с гс, я жаловаться админу')
        bot.send_voice(message.chat.id, file_id)
    
    @bot.message_handler(content_types=["video"])
    def video(message):
        file_id = message.video.file_id
        bot.send_message(message.chat.id, 'просто иди в жопу')
        bot.send_video(message.chat.id, file_id)    

    @bot.message_handler(content_types=["photo"])
    def photo(message):
        file_id = message.photo[0].file_id
        bot.send_message(message.chat.id, 'Опа поставлю себе на аватрку')
        bot.send_photo(message.chat.id, file_id)

    def database(message): 
        us_id = message.from_user.id 
        info = cursor.execute('SELECT * FROM users_Kimberg WHERE user_id=?', (us_id, )) 
        if info.fetchone() is None:      
            dt = datetime.datetime.now() 
            dt = dt.strftime(dt.strftime("Day: %d/%m/%Y  time: %H:%M:%S"))           
            us_name = message.from_user.first_name
            us_sname = message.from_user.last_name
            username = message.from_user.username
            database_add(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username, datetime=dt) 
        
    def database_add(user_id: int, user_name: str, user_surname: str, username: str, datetime: str):
        cursor.execute('INSERT INTO users_Kimberg (user_id, user_name, user_surname, username, datetime) VALUES (?, ?, ?, ?, ?)', (user_id, user_name, user_surname, username, datetime))
        Kimberg.commit()


    def target_time(): 
        schedule.every(10).minutes.do(transfers_auto)
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = Thread(target=target_time)
    thread.start()

    bot.polling()

start_program()