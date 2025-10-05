import os
import requests
import sqlite3
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# 🔑 Токены из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# NEW: Твой user_id (для доступа к /stats). Замени на свой!
ADMIN_USER_ID = 293349337  # Получи через @userinfobot

# 🌐 URL OpenRouter
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# 📚 Словарь для переводов
LANGUAGES = {
    "ru": {
        "greeting":
        "Привет! Я Асал, твой ИИ-бот на OpenRouter 🤖.",
        "response_error":
        "Ошибка: что-то пошло не так. Попробуй ещё раз!",
        "language_set":
        "Язык установлен: Русский",
        "system_prompt":
        "Ты — дружелюбный Telegram-бот по имени Асал. Отвечай на русском языке.",
        "help_text":
        "Я Асал, твой ИИ-бот! Используй /start, чтобы выбрать язык, или просто пиши мне, и я отвечу на твоём языке."
    },
    "uz": {
        "greeting":
        "Salom! Men Asal, OpenRouter tomonidan ishlaydigan AI botman 🤖.",
        "response_error":
        "Xato: nimadir noto'g'ri bo'ldi. Qayta urinib ko'ring!",
        "language_set":
        "Til o'rnatildi: O'zbek",
        "system_prompt":
        "Siz Asal ismli do'stona Telegram botisiz. O'zbek tilida javob bering.",
        "help_text":
        "Men Asal, sizning AI botingiz! Tilni tanlash uchun /start buyrug'ini ishlating yoki shunchaki yozing, men sizning tilingizda javob beraman."
    },
    "en": {
        "greeting":
        "Hello! I'm Asal, your AI bot powered by OpenRouter 🤖.",
        "response_error":
        "Error: something went wrong. Try again!",
        "language_set":
        "Language set: English",
        "system_prompt":
        "You are a friendly Telegram bot named Asal. Respond in English.",
        "help_text":
        "I'm Asal, your AI bot! Use /start to choose a language or just write to me, and I'll respond in your language."
    }
}


# Функция для инициализации БД
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            first_active_date TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Функция для добавления пользователя
def add_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT OR IGNORE INTO users (user_id, first_active_date) VALUES (?, ?)',
        (user_id, datetime.now().isoformat()))
    conn.commit()
    conn.close()


# Функция для подсчёта пользователей
def get_user_count():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    conn.close()
    return count


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_user(user_id)

    keyboard = [[
        InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="lang_uz"),
        InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    greeting = (f"{LANGUAGES['ru']['greeting']}\n"
                f"{LANGUAGES['uz']['greeting']}\n"
                f"{LANGUAGES['en']['greeting']}\n\n"
                "Выбери язык / Tilni tanlang / Choose a language:")

    await update.message.reply_text(greeting, reply_markup=reply_markup)
    context.user_data["chat_history"] = []


async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    add_user(user_id)

    lang = query.data.split("_")[1]
    context.user_data["language"] = lang

    await query.message.reply_text(LANGUAGES[lang]["language_set"])
    await query.message.delete()


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("language", "ru")
    await update.message.reply_text(LANGUAGES[lang]["help_text"])


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_USER_ID:
        await update.message.reply_text("❌ У тебя нет доступа к этой команде.")
        return

    count = get_user_count()
    await update.message.reply_text(
        f"📊 Статистика бота:\nВсего уникальных пользователей: {count}")


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_user(user_id)

    lang = context.user_data.get("language", "ru")
    user_message = update.message.text

    if "chat_history" not in context.user_data:
        context.user_data["chat_history"] = []
    context.user_data["chat_history"].append({
        "role": "user",
        "content": user_message
    })

    chat_history = context.user_data["chat_history"][-10:]

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model":
        "openai/gpt-3.5-turbo",
        "messages": [{
            "role": "system",
            "content": LANGUAGES[lang]["system_prompt"]
        }, *chat_history]
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=data)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        context.user_data["chat_history"].append({
            "role": "assistant",
            "content": reply
        })
    else:
        reply = LANGUAGES[lang]["response_error"]

    await update.message.reply_text(reply)


def main():
    init_db()
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(CallbackQueryHandler(set_language, pattern="^lang_"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Бот Асал запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
