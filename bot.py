import telebot
import os
import logging

# Setup logging (biar gampang debug di Railway)
logging.basicConfig(level=logging.INFO)

# Ambil token dari environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Pastikan token tidak kosong
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN tidak ditemukan! Pastikan sudah diset di Railway.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Halo! Aku bot yang berjalan di Railway! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Kamu berkata: {message.text}")

if __name__ == "__main__":
    logging.info("Bot sedang berjalan...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
