import logging 

from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv

# 🔥 Set up logging immediately after imports

logging.basicConfig(
format
=
'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
, level=logging.INFO)

# Load environment variables from .env file

load_dotenv()

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получаем токен бота из переменной окружения
TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise ValueError("Токен не найден! Пожалуйста, убедитесь, что переменная окружения 'TOKEN' установлена.")

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
    "0.1": ["Вы молились о том, чтобы Бог вселил в вас и в участников этой группы великий страх перед грехом прелюбодеяния?", "Вы постились по этому поводу?"],
    "1": ["Вы молились о том, чтобы исполниться Духом Святым?"]
}

# Основная логика вашего бота должна быть здесь
if __name__ == "__main__":  # No indentation before this
    logging.info("Bot started. Configuring handlers and starting polling.")
    
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    
    try:  # Indent this line with 4 spaces
        application.run_polling()  # Indent with 4 spaces after `try:`
    except Exception as e:  # Indent this line with 4 spaces to match the `try`
        logging.error(f"Error while running the bot: {e}")  # Indent with 8 spaces inside the except block

