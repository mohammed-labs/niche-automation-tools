import telebot

API_KEY = "your-telegram-bot-api-key"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send your details to generate a lead.")

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    # Save lead (just print for now)
    print(f"New lead: {message.text}")
    bot.reply_to(message, "Thanks! Your lead has been captured.")

bot.polling()
