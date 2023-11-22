from django.core.management.base import BaseCommand
from shop.models import Product, Video
import telebot

bot = telebot.TeleBot("6948290779:AAGJgiMOwcr6qxp7Tod1YHnlb_S2DlZPbpQ")
is_wait = false

def is_waiting():
    return is_wait

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот который сохраняет в себе видео. Команды: /add и /videos")

@bot.message_handler(commands=['products'])
def products(message):
    products = Product.objects.all()
    for product in products:
        bot.send_message(message.chat.id, f"Name: {product.name}, Price: {product.price}")

@bot.message_handler(commands=['videos'])
def videos(message):
    videos = Video.objects.all()
    for video in videos:
        bot.send_message(message.chat.id, f"Название: {video.name}, URL: {video.url}")

@bot.message_handler(commands=['add'])
def add(message):
    is_wait = True
    name = title_handler(message)
    url = url_handler(message)

    new_video = Video.objects.create(name=name, url=url)

@bot.message_handler(func=is_waiting)
def title_handler(message):
    bot.send_message(message.chat.id, f"Напишите название видео")
    title = message.text
    bot.send_message(message.chat.id, f"{title}")

@bot.message_handler(func=is_waiting)
def url_handler(message, video):
    bot.send_message(message.chat.id, f"Вставьте URL видео")
    url = message.text
    video.url = url


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

