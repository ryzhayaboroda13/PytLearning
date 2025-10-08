# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ТОКЕН, который ты получил от @BotFather
BOT_TOKEN = ""  # ← ЗАМЕНИ ЭТУ СТРОКУ!

# Функция, которая обрабатывает команду /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет приветственное сообщение когда пользователь пишет /start"""
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f"Привет, {user_name}! 👋\nЯ твой первый бот! Напиши мне что-нибудь!")

# Функция, которая обрабатывает команду /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет справку когда пользователь пишет /help"""
    help_text = """
    Доступные команды:
    /start - начать работу
    /help - получить помощь
    /about - о боте
    
    Просто напиши мне что-нибудь, и я отвечу!
    """
    await update.message.reply_text(help_text)

# Функция, которая обрабатывает команду /about
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет информацию о боте"""
    about_text = """
    🤖 Это мой первый телеграм-бот!
    Создан с помощью Python и библиотеки python-telegram-bot.
    Автор: Daniel (при поддержке AI-помощника)
    """
    await update.message.reply_text(about_text)

# Функция, которая отвечает на обычные текстовые сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает все текстовые сообщения"""
    user_text = update.message.text
    user_name = update.message.from_user.first_name
    
    # Простой эхо-ответ с небольшими вариациями
    responses = [
        f"{user_name}, ты написал: '{user_text}'",
        f"Получил твое сообщение: '{user_text}' 👍",
        f"Запомнил: '{user_text}' 📝",
        f"Интересное сообщение: '{user_text}' 🤔"
    ]
    
    # Выбираем случайный ответ из списка
    import random
    response = random.choice(responses)
    await update.message.reply_text(response)

# Функция, которая обрабатывает ошибки
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает ошибки которые могут возникнуть"""
    print(f"Произошла ошибка: {context.error}")

# Основная функция которая запускает бота
def main():
    """Главная функция которая настраивает и запускает бота"""
    print("Запускаю бота...")
    
    # Создаем приложение с нашим токеном
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    
    # Добавляем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Добавляем обработчик ошибок
    application.add_error_handler(error_handler)
    
    # Запускаем бота (будет постоянно опрашивать сервер Telegram)
    print("Бот запущен! Найди его в Telegram и напиши /start")
    application.run_polling()

# Точка входа в программу
if __name__ == "__main__":
    main()