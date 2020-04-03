import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def welcome(message):
	bot.send_message(message.chat.id , "Welcome to SuSanya's Support_Bot!")

@bot.message_handler(content_types = ['text'])
def echo_mess(message):
	bot.send_message(message.chat.id , message.text)

#Run
bot.polling(none_stop = True)