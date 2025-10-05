# 🤖 Asal – Telegram AI Bot

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)  
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)](https://t.me/)  
[![OpenRouter](https://img.shields.io/badge/OpenRouter-GPT--3.5--turbo-orange)](https://openrouter.ai/)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)  
[![Author](https://img.shields.io/badge/Made%20by-@sadullaevich__f-blueviolet?logo=telegram)](https://t.me/sadullaevich_f)

Многоязычный Telegram-чатбот на базе **OpenRouter API (GPT-3.5-turbo)**.  
Поддерживает **русский, узбекский и английский языки**, ведёт историю диалога и собирает аналитику по пользователям.  

---

## 🚀 Возможности

- 🌍 **Мультиязычная поддержка**: RU 🇷🇺, UZ 🇺🇿, EN 🇬🇧  
- 🤝 **AI-чат**: интеграция с GPT-3.5-turbo (OpenRouter API)  
- 💬 **История сообщений**: сохраняет последние 10 сообщений каждого пользователя  
- 📊 **Аналитика**: отслеживает уникальных пользователей и дату первого визита  
- 🔒 **Админ-панель**: доступ к статистике только у администратора  

---

## 📂 Архитектура проекта

- `main.py` – основной файл бота (хэндлеры и AI-интеграция)  
- `users.db` – база SQLite для отслеживания пользователей  
- `.gitignore` – исключает кэш, виртуальные окружения и БД  

---

## 📜 Команды бота

- `/start` – выбор языка через inline-клавиатуру  
- `/help` – помощь на выбранном языке  
- `/stats` – статистика (только для админа)  

---

## ⚙️ Установка и запуск

1. **Клонируй репозиторий**  
   ```bash
   git clone https://github.com/alibayev03/YordamchiDP_bot.git
   cd YordamchiDP_bot

2. Установи зависимости
pip install -r requirements.txt
python-telegram-bot==20.7

requests==2.31.0

3. Создай .env файл (или используй секреты хостинга):

TELEGRAM_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key
4. ⚠️ Убедись, что TELEGRAM_TOKEN – это токен от BotFather
(пример: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz),
а не ключ от OpenRouter.

Запусти бота

python main.py


При первом запуске автоматически создастся база users.db.

☁️ Деплой на Render.com

Ты можешь легко запустить бота на Render
:

Создай новый Web Service на Render

Подключи свой GitHub-репозиторий

В настройках установи:

Start Command:

python main.py


Environment Variables:

TELEGRAM_TOKEN

OPENROUTER_API_KEY

Сохрани и перезапусти сервис – бот будет работать 24/7.

🛠️ Текущий статус

✅ Код готов к запуску

✅ Настроена база SQLite

✅ Установлены зависимости

✅ Admin User ID: 293349337

✅ Workflow настроен

🗓️ Недавние изменения

Oct 5, 2025

Инициализация проекта

Перенос кода в main.py

Установка Python 3.11 + пакетов

Создание .gitignore

Добавлен Admin User ID

Настроен workflow

🔧 Решение проблем

❌ Бот не запускается → проверь консоль и правильность токенов

❌ Нет ответа в Telegram → убедись, что бот работает и хостинг активен

❌ Ограничения Replit → при превышении лимитов CPU использовать Render.com или PythonAnywhere

👤 Создатель

Разработчик: @sadullaevich_f

🤝 Contributing

Форкни репозиторий, улучшай проект и создавай Pull Request.

📄 Лицензия

MIT License (см. LICENSE
)

🌐 Репозиторий

👉 GitHub – YordamchiDP_bot
