import telebot #отвечает за связь с телеграм
from telebot import types #отвечает за связь с телеграм
from bs4 import BeautifulSoup #с помощью него вытаскиваю данные из полученного html
import undetected_chromedriver as uc #управление физическим браузером
import settigs_post #настройки
import time #отвечает за действия со временем условно отложить на 5 сек
import traceback

user_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Выложить пост")
user_main.add(item1)

markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Вернуться в меню")
markup_back.add(item1)

make_post = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Сделать пост в мужской паблик")
item2 = types.KeyboardButton("Сделать пост в женский паблик")
item3 = types.KeyboardButton("Вернуться в меню")
make_post.add(item1, item2, item3)

post = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Сделать пост")
item2 = types.KeyboardButton("Вернуться в меню")
post.add(item1, item2)

category_merch = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("#аниме")
item2 = types.KeyboardButton("#кофты")
item3 = types.KeyboardButton("#футболки")
item4 = types.KeyboardButton("#кепки")
item5 = types.KeyboardButton("#шапки")
item6 = types.KeyboardButton("#шарфы")
item7 = types.KeyboardButton("#штаны")
item8 = types.KeyboardButton("#шорты")
item9 = types.KeyboardButton("#свитера")
item10 = types.KeyboardButton("#очки")
item11 = types.KeyboardButton("#ночники")
item12 = types.KeyboardButton("#ремни")
item13 = types.KeyboardButton("#сумки")
item14 = types.KeyboardButton("#рубашки")
item15 = types.KeyboardButton("#куртки")
item16 = types.KeyboardButton("#пальто")
item17 = types.KeyboardButton("#ветровки")
item18 = types.KeyboardButton("#бомберы")
item19 = types.KeyboardButton("#бижутерия")
item20 = types.KeyboardButton("#обувь")
item21 = types.KeyboardButton("#носки")
item22 = types.KeyboardButton("#пижамы")
item23 = types.KeyboardButton("#снуды")
item24 = types.KeyboardButton("#перчатки")
item25 = types.KeyboardButton("#1000мелочей")
item26 = types.KeyboardButton("#спорттовары")
item27 = types.KeyboardButton("#сеты")
item28 = types.KeyboardButton("#часы")
item29 = types.KeyboardButton("Вернуться в меню")
category_merch.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27, item28, item29)

category_merch_girl = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("#аниме")
item2 = types.KeyboardButton("#свитера")
item3 = types.KeyboardButton("#перчатки")
item4 = types.KeyboardButton("#сумки")
item5 = types.KeyboardButton("#шапки")
item6 = types.KeyboardButton("#футболки")
item7 = types.KeyboardButton("#кофты")
item8 = types.KeyboardButton("#кардиганы")
item9 = types.KeyboardButton("#пижамы")
item10 = types.KeyboardButton("#куртки")
item11 = types.KeyboardButton("#бижутерия")
item12 = types.KeyboardButton("#кепки")
item13 = types.KeyboardButton("#носки")
item14 = types.KeyboardButton("#ободки")
item15 = types.KeyboardButton("#рюкзаки")
item16 = types.KeyboardButton("#рубашки")
item17 = types.KeyboardButton("#топы")
item18 = types.KeyboardButton("#платья")
item19 = types.KeyboardButton("#ночники")
item20 = types.KeyboardButton("#очки")
item21 = types.KeyboardButton("#обувь")
item22 = types.KeyboardButton("#1000мелочей")
item23 = types.KeyboardButton("#юбки")
item24 = types.KeyboardButton("#колготки")
item25 = types.KeyboardButton("#спорттовары")
item26 = types.KeyboardButton("#чокеры ")
item27 = types.KeyboardButton("#штаны")
item28 = types.KeyboardButton("#педжаки")
item29 = types.KeyboardButton("Вернуться в меню")
category_merch_girl.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27, item28, item29)

channel_boy = settigs_post.channel_boy
channel_girl = settigs_post.channel_girl
post_info_1 = []
post_info_2 = []
post_info_3 = []
pohoto_info = []
chat_id = 1949227825

def start_program():
    token = settigs_post.token
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])    
    def welcome(message):
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>🤖, бот для создания постов ".format(message.from_user, bot.get_me()),
       parse_mode='html', reply_markup=user_main)
    
    @bot.message_handler(content_types=['text'])
    def lalala(message):
        if message.text == 'Выложить пост':
            post_info_1.clear()
            post_info_2.clear()
            post_info_3.clear()
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=make_post)
            bot.register_next_step_handler(message, choose_publik)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
        else:
            bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку')

    def choose_publik(message):
        if message.text == 'Сделать пост в мужской паблик':
            male = 'муж'
        elif message.text == 'Сделать пост в женский паблик':
            male = 'жен'
        bot.send_message(message.chat.id, 'Пришлите пожалуйста ссылку 1', reply_markup=markup_back)
        bot.register_next_step_handler(message, create_post_link_1, male)

    def request(message, link, driver):
        if message.text !='Вернуться в меню':
            try:
                driver.get(link) 
                time.sleep(5)
                response = driver.page_source.encode('utf-8')
                soup = BeautifulSoup(response, 'lxml')
                reiting = soup.find('span', class_='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1').text
                try:
                    cost = soup.find('span', class_='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 price ali-kit_Price__size-xl__12ybyf Product_Price__current__1uqb8 product-price-current').text
                except:
                    cost = soup.find('span', class_='Product_UniformBanner__uniformBannerBoxPrice__o5qwb').text
                photo = soup.find_all('img', class_="ali-kit_Image__image__1jaqdj")
                prise_dostavka = soup.find('span', class_='freight-extra-info-detail').text
                prise_dostavka = prise_dostavka.replace("руб.", '').replace(",", '.').replace("\xa0", '').replace(" ", '').replace("за", '')
                cost = cost.replace("руб.", '').replace(",", '.').replace("\xa0", '').replace(" ", '')
                cost_min = cost.split('-')[0]
                cost_max = cost.split('-')[-1]
                if cost_min == cost_max and prise_dostavka != 'Бесплатно':
                    prise_dostavka = float(prise_dostavka)
                    cost_min = float(cost_min)
                    cost = (f'{prise_dostavka + cost_min}₽')
                elif cost_min != cost_max and prise_dostavka != 'Бесплатно':
                    prise_dostavka = float(prise_dostavka)
                    cost_min = float(cost_min)
                    cost_max = float(cost_max)
                    cost = (f'{prise_dostavka + cost_min}₽ - {prise_dostavka + cost_max}₽')
                elif cost_min == cost_max and prise_dostavka == 'Бесплатно':
                    cost = (f'{cost_min}₽')
                elif cost_min != cost_max and prise_dostavka == 'Бесплатно':
                    cost = (f'{cost_min}₽ - {cost_max}₽')
                return(reiting, cost, photo)
            except:
                bot.send_message(chat_id, traceback.format_exc())
                bot.send_message(message.chat.id, f'Выполни капчу и напиши что-то мне')
                bot.register_next_step_handler(message, request, link, driver)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            driver.quit()

    def create_post_link_1(message, male):
        if message.text != 'Вернуться в меню':
            driver = uc.Chrome()#(options=options)
            pohoto_info.clear()
            check_link = "http://al" in message.text
            if check_link == True:
                link_1 = message.text
                try:
                    reiting_1, cost_1, photo_group_1 = request(message, link_1, driver)
                    cost_1 = cost_1.split(' - ')[-1]
                    cost_1 = cost_1.replace(" руб.", '₽').replace(" - ", '₽ - ')
                    numb = 0
                    for photo in photo_group_1:
                        if  ".jpg_50x50" in photo['src']:
                            photo = photo['src']
                            photo = photo.replace(".jpg_50x50", '').replace("-", '')
                            numb = numb + 1
                            pohoto_info.append(photo)
                            bot.send_photo(message.chat.id, photo, caption=f'Номер фото - {numb}')
                    post_info_1.append(cost_1)
                    post_info_1.append(reiting_1)
                    post_info_1.append(link_1)
                    bot.send_message(message.chat.id, 'Выберите номер фото')
                    bot.register_next_step_handler(message, create_post_numb_1_1, male, driver)
                except:
                    None
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            driver.quit()

    def create_post_numb_1_1(message, male, driver):
        if message.text != 'Вернуться в меню':
            try: 
                numb = int(message.text) - 1
                post_info_1.append(pohoto_info[numb])
                bot.send_message(message.chat.id, 'Введите номер для фото 2')
                bot.register_next_step_handler(message, create_post_numb_1, male, driver)
            except:
                try:
                    idphoto = message.photo[0].file_id
                    bot.send_photo(message.chat.id, idphoto, caption='провека на возможность отправить это фото')
                    post_info_1.append(idphoto) 
                    bot.send_message(message.chat.id, 'Введите номер для фото 2')
                    bot.register_next_step_handler(message, create_post_numb_1, male, driver)
                except:
                    bot.send_message(message.chat.id, 'Неккоректный номер, по пробуйте ещё раз')
                    bot.register_next_step_handler(message, create_post_numb_1_1, male, driver)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            driver.quit()

    def create_post_numb_1(message, male, driver):
        if message.text != 'Вернуться в меню':
            try: 
                numb = int(message.text) - 1
                post_info_1.append(pohoto_info[numb])
                if male == 'муж':
                    bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch)
                elif male == 'жен':
                    bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch_girl)
                bot.register_next_step_handler(message, create_post_category_1, male, driver)
            except:
                try:
                    idphoto = message.photo[0].file_id
                    bot.send_photo(message.chat.id, idphoto, caption='провека на возможность отправить это фото')
                    post_info_1.append(idphoto) 
                    if male == 'муж':
                        bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch)
                    elif male == 'жен':
                        bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch_girl)
                    bot.register_next_step_handler(message, create_post_category_1, male, driver)
                except:
                    bot.send_message(message.chat.id, 'Неккоректный номер, по пробуйте ещё раз')
                    bot.register_next_step_handler(message, create_post_numb_1, male, driver)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            driver.quit()

    def create_post_category_1(message, male, driver):
        if message.text != 'Вернуться в меню':
            post_info_1.append(message.text)
            bot.send_message(message.chat.id, 'Пришлите пожалуйста ссылку 2', reply_markup=markup_back)
            bot.register_next_step_handler(message, create_post_link_2, male, driver)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            driver.quit()

    def create_post_link_2(message, male, driver):
        if message.text != 'Вернуться в меню':
            pohoto_info.clear()
            check_link = "http://al" in message.text
            if check_link == True:
                link_2 = message.text
                reiting_2, cost_2, photo_group_2 = request(message, link_2, driver)
                cost_2 = cost_2.split(' - ')[-1]
                cost_2 = cost_2.replace(" руб.", '₽').replace(" - ", '₽ - ')
                numb = 0
                for photo in photo_group_2:
                    if  ".jpg_50x50" in photo['src']:
                        photo = photo['src']
                        photo = photo.replace(".jpg_50x50", '')
                        numb = numb + 1
                        pohoto_info.append(photo)
                        bot.send_photo(message.chat.id, photo, caption=f'Номер фото - {numb}')
                    else:
                        None
                post_info_2.append(cost_2)
                post_info_2.append(reiting_2)
                post_info_2.append(link_2)
                bot.send_message(message.chat.id, 'Выберите номер фото')
                bot.register_next_step_handler(message, create_post_numb_2_1, male, driver)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            driver.quit()

    def create_post_numb_2_1(message, male, driver):
        if message.text != 'Вернуться в меню':
            try: 
                numb = int(message.text) - 1
                post_info_2.append(pohoto_info[numb])
                bot.send_message(message.chat.id, 'Выберите номер фото 2')
                bot.register_next_step_handler(message, create_post_numb_2, male, driver)
            except:
                try:
                    idphoto = message.photo[0].file_id
                    bot.send_photo(message.chat.id, idphoto, caption='провека на возможность отправить это фото')
                    post_info_2.append(idphoto) 
                    bot.send_message(message.chat.id, 'Выберите номер фото 2')
                    bot.register_next_step_handler(message, create_post_numb_2, male, driver)
                except:
                    bot.send_message(message.chat.id, 'Неккоректный номер, по пробуйте ещё раз')
                    bot.register_next_step_handler(message, create_post_numb_2_1, male, driver)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            driver.quit()

    def create_post_numb_2(message, male, driver):
        if message.text != 'Вернуться в меню':
            try: 
                numb = int(message.text) - 1
                post_info_2.append(pohoto_info[numb])
                if male == 'муж':
                    bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch)
                elif male == 'жен':
                    bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch_girl)
                bot.register_next_step_handler(message, create_post_category_2, male, driver)
            except:
                try:
                    idphoto = message.photo[0].file_id
                    bot.send_photo(message.chat.id, idphoto, caption='провека на возможность отправить это фото')
                    post_info_2.append(idphoto) 
                    if male == 'муж':
                        bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch)
                    elif male == 'жен':
                        bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch_girl)
                    bot.register_next_step_handler(message, create_post_category_2, male, driver)
                except:
                    bot.send_message(message.chat.id, 'Неккоректный номер, по пробуйте ещё раз')
                    bot.register_next_step_handler(message, create_post_numb_2, male, driver)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            driver.quit()

    def create_post_category_2(message, male, driver):
        if message.text != 'Вернуться в меню':
            post_info_2.append(message.text)
            bot.send_message(message.chat.id, 'Пришлите пожалуйста ссылку 3', reply_markup=markup_back)
            bot.register_next_step_handler(message, create_post_link_3, male, driver)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            driver.quit()
            
    def create_post_link_3(message, male, driver):
        if message.text != 'Вернуться в меню':
            pohoto_info.clear()
            check_link = "http://al" in message.text
            if check_link == True:
                link_3 = message.text
                reiting_3, cost_3, photo_group_3 = request(message, link_3, driver)
                driver.quit()
                cost_3 = cost_3.split(' - ')[-1]
                cost_3 = cost_3.replace(" руб.", '₽').replace(" - ", '₽ - ')
                numb = 0
                for photo in photo_group_3:
                    if  ".jpg_50x50" in photo['src']:
                        photo = photo['src']
                        photo = photo.replace(".jpg_50x50", '')
                        numb = numb + 1
                        pohoto_info.append(photo)
                        bot.send_photo(message.chat.id, photo, caption=f'Номер фото - {numb}')
                    else:
                        None
                post_info_3.append(cost_3)
                post_info_3.append(reiting_3)
                post_info_3.append(link_3)
                bot.send_message(message.chat.id, 'Выберите номер фото')
                bot.register_next_step_handler(message, create_post_numb_3_1, male)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
        
    def create_post_numb_3_1(message, male):
        if message.text != 'Вернуться в меню':
            try: 
                numb = int(message.text) - 1
                post_info_3.append(pohoto_info[numb])
                bot.send_message(message.chat.id, 'пришлите номер для фото 2')
                bot.register_next_step_handler(message, create_post_numb_3, male)
            except:
                try:
                    idphoto = message.photo[0].file_id
                    bot.send_photo(message.chat.id, idphoto, caption='провека на возможность отправить это фото')
                    post_info_3.append(idphoto) 
                    bot.send_message(message.chat.id, 'пришлите номер для фото 2')
                    bot.register_next_step_handler(message, create_post_numb_3, male)
                except:
                    bot.send_message(message.chat.id, 'Неккоректный номер, по пробуйте ещё раз')
                    bot.register_next_step_handler(message, create_post_numb_3_1, male)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)

    def create_post_numb_3(message, male):
        if message.text != 'Вернуться в меню':
            try: 
                numb = int(message.text) - 1
                post_info_3.append(pohoto_info[numb])
                if male == 'муж':
                    bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch)
                elif male == 'жен':
                    bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch_girl)
                bot.register_next_step_handler(message, create_post_category_3, male)
            except:
                try:
                    idphoto = message.photo[0].file_id
                    bot.send_photo(message.chat.id, idphoto, caption='провека на возможность отправить это фото')
                    post_info_3.append(idphoto) 
                    if male == 'муж':
                        bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch)
                    elif male == 'жен':
                        bot.send_message(message.chat.id, 'Выберите хэштэг', reply_markup=category_merch_girl)
                    bot.register_next_step_handler(message, create_post_category_3, male)
                except:
                    bot.send_message(message.chat.id, 'Неккоректный номер, по пробуйте ещё раз')
                    bot.register_next_step_handler(message, create_post_numb_3)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)

    def create_post_category_3(message, male):
        if message.text != 'Вернуться в меню':
            post_info_3.append(message.text)
            medias = [types.InputMediaPhoto(f'{post_info_1[3]}', caption=f'{post_info_1[5]}\n💸{post_info_1[0]}\n🌟{post_info_1[1]}/5\n~ {post_info_1[2]}\n\n{post_info_2[5]}\n💸{post_info_2[0]}\n🌟{post_info_2[1]}/5\n~ {post_info_2[2]}\n\n{post_info_3[5]}\n💸{post_info_3[0]}\n🌟{post_info_3[1]}/5\n~ {post_info_3[2]}'), types.InputMediaPhoto(f'{post_info_1[4]}'), types.InputMediaPhoto(f'{post_info_2[3]}'), types.InputMediaPhoto(f'{post_info_2[4]}'), types.InputMediaPhoto(f'{post_info_3[3]}'), types.InputMediaPhoto(f'{post_info_3[4]}')]
            bot.send_media_group(message.chat.id, medias)
            bot.send_message(message.chat.id, 'Выложить пост?', reply_markup=post)
            bot.register_next_step_handler(message, post_previe, male)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
            
    def post_previe(message, male):
        if message.text == 'Сделать пост':
            medias = [types.InputMediaPhoto(f'{post_info_1[3]}', caption=f'{post_info_1[5]}\n💸{post_info_1[0]}\n🌟{post_info_1[1]}/5\n~ {post_info_1[2]}\n\n{post_info_2[5]}\n💸{post_info_2[0]}\n🌟{post_info_2[1]}/5\n~ {post_info_2[2]}\n\n{post_info_3[5]}\n💸{post_info_3[0]}\n🌟{post_info_3[1]}/5\n~ {post_info_3[2]}'), types.InputMediaPhoto(f'{post_info_1[4]}'), types.InputMediaPhoto(f'{post_info_2[3]}'), types.InputMediaPhoto(f'{post_info_2[4]}'), types.InputMediaPhoto(f'{post_info_3[3]}'), types.InputMediaPhoto(f'{post_info_3[4]}')]
            if male == 'муж':
                bot.send_media_group(channel_boy, medias)
                bot.send_message(message.chat.id, 'Пост выложен', reply_markup=user_main)
            elif male == 'жен':
                bot.send_media_group(channel_girl, medias)
                bot.send_message(message.chat.id, 'Пост выложен', reply_markup=user_main)
        elif message.text == 'Вернуться в меню':
            bot.send_message(message.chat.id, 'вы вернулись', reply_markup=user_main)
        else:
            bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку')
            bot.register_next_step_handler(message, post_previe)
    
    bot.polling()

if __name__ == '__main__':
    while True:
        try:
            start_program()
        except Exception:
            print(traceback.format_exc())