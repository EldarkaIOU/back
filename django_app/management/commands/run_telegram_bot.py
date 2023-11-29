from django.core.management.base import BaseCommand
import telebot
from django_app.models import Car

bot = telebot.TeleBot("5801396304:AAF2SBjR6ZkgAsqQ1m64S5fRQjrnw_s77AI")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['Cars'])
def show_cars(message):
    cars = Car.objects.all()
    for car in cars:
        bot.send_message(message.chat.id, car.name)


@bot.message_handler(commands=['help'])
def help_command(message):
    help_message = "Commands:\n" \
                   "/start - Start the bot\n" \
                   "/Cars - Get information about Cars\n" \
                   "/help - Display this help message"

    bot.send_message(message.chat.id, help_message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")


