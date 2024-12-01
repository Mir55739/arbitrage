from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
const = 227
# Глобальные переменные для отслеживания состояния диалога
current_state = None
ADD_TO_BLACKLIST, REMOVE_FROM_BLACKLIST = range(1, 3)
# Инициализация словаря для хранения настроек каждого чата
chat_settings = {}
blacklist = []

# Список разрешенных идентификаторов чатов
allowed_chat_ids = [600209729, 612868840, 834107383]


def start(update: Update, context):
    global current_state
    current_state = None
    keyboard = [
        [KeyboardButton("Биржи"), KeyboardButton("Спред")],
        [KeyboardButton("Черный список")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)
