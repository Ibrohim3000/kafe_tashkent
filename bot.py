import telebot 
from telebot import types 
 
bot = telebot.TeleBot("5907616032:AAHjPhohwRc79UjxDtxEgoSJ_GXJtNvDr5o")
korzinka = []
@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == '/start':
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("Меню")
        menu.add(bt1)
        bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}, Что будем кушать".format(message.from_user, bot.get_me()), 
			reply_markup=menu)
    if message.text == 'Меню':
        kategoria = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Первые блюда")
        btn2 = types.KeyboardButton("Вторые блюда")
        btn3 = types.KeyboardButton("Салаты")
        btn4 = types.KeyboardButton("Напитки")
        btn5 = types.KeyboardButton("Корзинка")
        kategoria.add(btn1,btn2,btn3,btn4,btn5)
        bot.send_message(message.chat.id, "Выберите категорию".format(message.from_user, bot.get_me()), 
			reply_markup=kategoria)
    if message.text == "Первые блюда":
        blyuda1 = types.InlineKeyboardMarkup(row_width=2)
        bttn1 = types.InlineKeyboardButton("Мастава", callback_data="mastava")
        bttn2 = types.InlineKeyboardButton("Чучвара", callback_data="chuchvara")
        bttn3 = types.InlineKeyboardButton("Шурпа из говядины", callback_data="shurpa_gov")
        bttn4 = types.InlineKeyboardButton("Шурпа из баранины", callback_data="shurpa_bar")
        bttn5 = types.InlineKeyboardButton("Лагман уйгур", callback_data="lagman_uyg")
        blyuda1.add(bttn1, bttn2, bttn3, bttn4, bttn5)
        bot.send_message(message.chat.id, "Выберите блюдо", reply_markup=blyuda1)
    if message.text == "Вторые блюда":
        blyuda2 = types.InlineKeyboardMarkup(row_width=2)
        bttn1 = types.InlineKeyboardButton("Плов", callback_data="plov")
        bttn2 = types.InlineKeyboardButton("Лагман жаренный", callback_data="lagman_jar")
        bttn3 = types.InlineKeyboardButton("Коурдак", callback_data="kourdak")
        bttn4 = types.InlineKeyboardButton("Мясо острое", callback_data="myaso_ost")
        bttn5 = types.InlineKeyboardButton("Мясо жар. с овощ.", callback_data="myaso_jar")
        bttn6 = types.InlineKeyboardButton("Манты", callback_data="manti")
        bttn7 = types.InlineKeyboardButton("Самса", callback_data="samsa")
        bttn8 = types.InlineKeyboardButton("Сосиска в тесте", callback_data="sosiska")
        blyuda2.add(bttn1, bttn2, bttn3, bttn4, bttn5, bttn6,bttn7,bttn8)
        bot.send_message(message.chat.id, "Выберите блюдо", reply_markup=blyuda2)
    #if message.text == "Салаты":
    #if message.text == "Напитки":
    if message.text == "Корзинка":
        zakaz = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оформить заказ")
        zakaz.add(btn1)
        bot.send_message(message.chat.id, f"Ваш заказ {korzinka}", reply_markup=zakaz)
    if message.text == "Оформить заказ":
        oform = types.ReplyKeyboardMarkup(resize_keyboard=True)
        contact = types.KeyboardButton("Отправить контакт", request_contact=True)
        oform.add(contact)
        bot.send_message(message.chat.id, "Нажмите отправить контакт", reply_markup=oform)
@bot.message_handler(content_types=['contact'])
def check_contact(message):
    global contact
    contact = message.contact.phone_number
    location = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("Отправить локацию", request_location=True)
    location.add(bt1)
    bot.send_message(message.chat.id, "Куда доставить", reply_markup=location)
@bot.message_handler(content_types=['location'])
def location(message):
    #global location
    #location = message.location
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("Меню")
    menu.add(bt1)
    bot.send_message(message.chat.id, "Заказ оформлен", reply_markup=menu)
    bot.send_message('@kafe_tashkent_zakaz', f' Новый заказ {korzinka}')
    bot.send_contact('@kafe_tashkent_zakaz', phone_number = contact, first_name='alex', last_name='alex')
    bot.send_location('@kafe_tashkent_zakaz', message.location.latitude, message.location.longitude)
@bot.callback_query_handler(func=lambda call:True)
def knadf(call):
    if call.message:
        if call.data == 'mastava':
            korzinka.append("Мастава")
            bot.answer_callback_query(call.id, text="Мастава добавлена в корзину")
        if call.data == 'chuchvara':
            korzinka.append("Чучвара")
            bot.answer_callback_query(call.id, text="Чучвара добавлена в корзину")
        if call.data == 'shurpa_gov':
            korzinka.append("Шурпа из говядины")
            bot.answer_callback_query(call.id, text="Шурпа из говядины добавлена в корзину")
        if call.data == 'shurpa_bar':
            korzinka.append("Шурпа из баранины")
            bot.answer_callback_query(call.id, text="Шурпа из баранины добавлена в корзину")
        if call.data == 'lagman_uyg':
            korzinka.append("Лагман уйгур")
            bot.answer_callback_query(call.id, text="Лагман уйгур добавлена в корзину")
        if call.data == 'plov':
            korzinka.append("Плов")
            bot.answer_callback_query(call.id, text="Плов добавлена в корзину")
        if call.data == 'lagman_jar':
            korzinka.append("Лагман жареный")
            bot.answer_callback_query(call.id, text="Лагман жареный добавлена в корзину")
        if call.data == 'kourdak':
            korzinka.append("Коурдак")
            bot.answer_callback_query(call.id, text="Коурдак добавлена в корзину")
        #bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text="Спасибо за выбор", reply_markup=None)

bot.polling(none_stop=True, interval=0)