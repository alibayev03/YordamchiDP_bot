Telegram AI Bot "Asal"
Overview
Multi-language Telegram AI chatbot powered by OpenRouter API (GPT-3.5-turbo). The bot supports Russian, Uzbek, and English languages with conversation history tracking and user analytics.
Current State

Bot code configured and ready to run
Dependencies installed (python-telegram-bot, requests)
SQLite database for user tracking
Admin user ID set: 293349337
Workflow configured to run automatically

Recent Changes

Oct 5, 2025: Initial project setup
Moved bot code to main.py
Installed Python 3.11 and required packages
Created .gitignore for Python projects
Set admin user ID to 293349337
Configured workflow to run bot



User Preferences

Admin User ID: 293349337

Project Architecture
Main Components

main.py: Core bot application with handlers and AI integration
users.db: SQLite database storing user tracking data
.gitignore: Excludes cache, virtual environments, and database files

Features

Multi-language Support: Russian (ru), Uzbek (uz), English (en)
AI Chat: OpenRouter API integration with GPT-3.5-turbo
Conversation History: Maintains last 10 messages per user
User Analytics: Tracks unique users and first active date
Admin Commands: Statistics command for admin only

Bot Commands

/start - Language selection with inline keyboard
/help - Display help message in user's language
/stats - Show user statistics (admin only)

Environment Variables Required

TELEGRAM_TOKEN - Bot token from @BotFather
OPENROUTER_API_KEY - API key from openrouter.ai
Admin User ID is hardcoded in main.py (currently: 293349337)

Installation and Setup

Clone or Download the Repository:
Clone this repo or download the files manually.


Install Dependencies:
Ensure Python 3.11 is installed.
Run pip install -r requirements.txt to install python-telegram-bot==20.7 and requests==2.31.0.


Configure Environment Variables:
Create a .env file or use a platform-specific secrets manager (e.g., Replit Secrets):TELEGRAM_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key


Important: Verify that TELEGRAM_TOKEN is your Telegram bot token (e.g., 123456789:ABCdefGHIjklMNOpqrsTUVwxyz), not the OpenRouter key.


Run the Bot:
Execute python main.py in your terminal or run via the hosting platform (e.g., Replit).
The bot will create users.db automatically on first run.



Important Notes

The bot requires a valid TELEGRAM_TOKEN to start. Ensure it matches the format 123456789:ABCdefGHIjklMNOpqrsTUVwxyz.
Current TELEGRAM_TOKEN may contain an incorrect value—double-check it’s your Telegram bot token, not the OpenRouter key.
The database file (users.db) is created automatically on the first run and stores user tracking data.

Usage

Start the bot with /start to select a language (Russian, Uzbek, or English).
Use /help for assistance in your chosen language.
Admins (user ID 293349337) can use /stats to view the number of unique users.

Troubleshooting

Bot not starting: Check the console for errors (e.g., invalid token) and verify environment variables.
No response in Telegram: Ensure the bot is running and the Replit instance is active (use Always On if available).
Resource limits: If CPU usage exceeds 100 seconds/day on Replit, consider optimizing the code or switching to a platform like PythonAnywhere.

Contributing
Feel free to fork this repository, make improvements, and submit pull requests!
License
MIT License (or specify your preferred license)
