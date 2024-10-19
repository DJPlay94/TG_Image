import telebot, os, random
    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("")
    
# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
@bot.message_handler(commands=['mem'])
def send_mem(message):
    random_image = random.choice(os.listdir("images"))
    with open(f'images/{random_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

# Запуск бота
bot.polling()
