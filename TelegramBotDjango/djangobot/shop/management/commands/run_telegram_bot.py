from django.core.management.base import BaseCommand
from shop.models import Product, Video
import telebot

bot = telebot.TeleBot("6948290779:AAGJgiMOwcr6qxp7Tod1YHnlb_S2DlZPbpQ")
video_list = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот который хранит твои сохранненые видео!\n Используй команды /add и /videos")

@bot.message_handler(commands=['videos'])
def videos(message):
    videos = Video.objects.all()
    for video in videos:
        bot.send_message(message.chat.id, f"Name: {video.name}, URL: {video.url}")

@bot.message_handler(commands=['add'])
def add_video(message):
    bot.reply_to(message, f"Напишите название видео")

    title_handler()

    new_product = Product.objects.create(name=product_name, price=product_price)

def title_handler(message):
    title = message.text
    bot.message.reply_text(f"Спасибо, вставьте пожалуйста URL видео")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

