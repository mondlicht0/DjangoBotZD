from django.core.management.base import BaseCommand
from shop.models import Product, Video
import telebot

bot = telebot.TeleBot("6948290779:AAGJgiMOwcr6qxp7Tod1YHnlb_S2DlZPbpQ")
is_adding = False

def is_add():
    return is_adding

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

def title_handler(message):
    bot.send_message(message.chat.id, f"Напишите название видео")
    title = message.text
    bot.register_next_step_handler(message, url_handler)

def url_handler(message, video):
    bot.send_message(message.chat.id, f"Вставьте URL видео")
    url = message.text
    video.url = url

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "/add /videos")
    elif message.text == "/add":
        bot.send_message("Введи название")
        bot.register_next_step_handler(message, title_handler)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

