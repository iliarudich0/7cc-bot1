from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters

# Вставьте сюда токен вашего бота
TOKEN = '7942164878:AAEvsE6uQsClEZhI12ikeUZ4sOxcyiecEPg'

# Определяем пункты меню
menu_items = {
    "0": "Молитва о себе и о участниках (7с), а также о новых молитвенниках если Господу это угодно",
    "0.1": "🔺Не упасть в грех прелюбодеяния",
    "1": "1. Исполняться Духом Святым",
    "1.1": "1.1. Всегда за все каяться",
    "1.2": "1.2. Постоянно быть послушным Иисусу",
    "1.3": "1.3. Всегда и полностью верить Иисусу",
    "4": "4. Пребывать в молитве",
    "5": "5. Изучать Слово",
    "6": "6. Иметь общение со святыми",
    "7": "7. Свидетельствовать об Иисусе"
}

# Вопросы по каждому пункту
questions = {
    "0": ["Вы молились о себе и об участниках группы?", "Вы просили Бога послать еще молитвенников?"],
    "0.1": ["Вы молились о том, чтобы Бог вселил в вас и в участников этой группы великий страх перед грехом прелюбодеяния?", "Вы постились по этой теме?"],
    "1": ["Вы стремились исполниться Духом Святым сегодня?", "Исполняли ли вы 3 закона духовной жизни?"],
    "1.1": ["Вы каялись сегодня за свои грехи?", "Какие грехи исповедовали пред Богом и людьми?"],
    "1.2": ["Были ли вы послушны Иисусу сегодня?", "Что в�� сделали, чтобы подчиниться воле Иисуса сегодня?"],
    "1.3": ["Вы верите Иисусу во всем?", "Вы доверяли Богу сегодня в своих делах и мыслях?"],
    "4": ["Вы молились сегодня?", "Как долго вы пребывали в молитве?"],
    "5": ["Вы изучали Слово сегодня?", "Какую часть Писания вы прочитали сегодня?"],
    "6": ["Вы имели общение со святыми сегодня?", "С кем из братьев и сестер вы сегодня общались?"],
    "7": ["Вы свидетельствовали об Иисусе сегодня?", "Кому вы рассказали об Иисусе сегодня?"],
}

# Словарь для хранения последних сообщений пользователей
user_last_message = {}

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    """Отправляет пользователю основное меню после команды /start и удаляет все предыдущие сообщения"""
    chat_id = update.message.chat_id

    # Удаляем текущее сообщение пользователя
    try:
        context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения /start: {e}")
    
    # Удаляем последнее сообщение с вопросами
    if chat_id in user_last_message:
        try:
            context.bot.delete_message(chat_id=chat_id, message_id=user_last_message[chat_id])
        except Exception as e:
            print(f"Ошибка при удалении сообщения: {e}")
    
    # Отправляем меню
    reply_markup = build_menu()
    message = context.bot.send_message(chat_id=chat_id, text="Начните проверку, выберите пункт из меню ниже:", reply_markup=reply_markup)
    user_last_message[chat_id] = message.message_id  # Сохраняем ID сообщения

# Функция для создания клавиатуры меню
def build_menu():
    """Создает и возвращает клавиатуру с пунктами меню"""
    keyboard = []
    for key, value in menu_items.items():
        keyboard.append([InlineKeyboardButton(value, callback_data=key)])
    return InlineKeyboardMarkup(keyboard)

# Обработка нажатий на кнопки
def button_handler(update: Update, context: CallbackContext) -> None:
    """Обрабатывает выбор пользователя в меню"""
    query = update.callback_query
    query.answer()
    
    # Получаем ключ пункта меню, по которому нажал пользователь
    selected_item = query.data
    item_title = menu_items.get(selected_item, "Неизвестный пункт")
    
    # Создаем текст с вопросами по выбранному пункту
    if selected_item in questions:
        question_list = questions[selected_item]
        message_text = f"<b>{item_title}</b>\n\nЗадайте себе эти вопросы, и перейдите к следующим пу��ктам.:"
        for i, question in enumerate(question_list, start=1):
            message_text += f"\n{i}. <i>{question}</i>"
    else:
        message_text = "Не удалось найти вопросы по этому пункту."

    # Добавляем меню в сообщение с вопросами
    message_text += "\n\n<b>Выберите другой пункт из меню ниже:</b>"
    reply_markup = build_menu()
    
    # Проверяем, отличается ли новое сообщение от текущего
    if query.message.text != message_text or query.message.reply_markup != reply_markup:
        query.edit_message_text(text=message_text, reply_markup=reply_markup, parse_mode='HTML')

def main() -> None:
    # Создаем Updater и передаем ему токен вашего бота
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl-C или получении сигнала завершения
    updater.idle()

if __name__ == '__main__':
    main()
