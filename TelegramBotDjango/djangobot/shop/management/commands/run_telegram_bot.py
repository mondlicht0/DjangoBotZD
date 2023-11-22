from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

# Словарь для хранения списка видео
video_list = {}

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для сохранения видео. Используй команды /add и /videos.')

# Обработчик команды /add
def add_video(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    text = update.message.text.replace('/add', '').strip()

    if chat_id not in video_list:
        video_list[chat_id] = []

    if text:
        video_list[chat_id].append(text)
        update.message.reply_text(f'Видео добавлено: {text}')
    else:
        update.message.reply_text('Пожалуйста, укажите ссылку на видео после /add.')

# Обработчик команды /videos
def list_videos(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id

    if chat_id in video_list and video_list[chat_id]:
        videos = "\n".join(video_list[chat_id])
        update.message.reply_text(f'Ваши видео:\n{videos}')
    else:
        update.message.reply_text('У вас пока нет сохраненных видео.')

# Обработчик текстовых сообщений (не команд)
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Извините, я понимаю только команды /add и /videos.')

# Добавляем обработчики команд
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('add', add_video))
updater.dispatcher.add_handler(CommandHandler('videos', list_videos))

# Добавляем обработчик текстовых сообщений (не команд)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Запускаем бота
updater.start_polling()

# Останавливаем бота при нажатии Ctrl+C
updater.idle()