from django.core.management.base import BaseCommand
from shop.models import Product, Video
import telebot

bot = telebot.TeleBot("6948290779:AAGJgiMOwcr6qxp7Tod1YHnlb_S2DlZPbpQ")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello World")

@bot.message_handler(commands=['products'])
def products(message):
    products = Product.objects.all()
    for product in products:
        bot.send_message(message.chat.id, f"Name: {product.name}, Price: {product.price}")

@bot.message_handler(commands=['videos'])
def videos(message):
    videos = Video.objects.all()
    for video in videos:
        bot.send_message(message.chat.id, f"Name: {video.name}, URL: {video.url}")

@bot.message_handler(commands=['add'])
def add(message):
    bot.reply_to(message, f"Напишите название видео")

    new_product = Product.objects.create(name=product_name, price=product_price)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

