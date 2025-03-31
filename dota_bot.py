from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import requests
import os

TOKEN = os.environ.get("TOKEN")
HEROES_DATA_URL = "https://api.stratz.com/api/v1/Hero"

heroes = requests.get(HEROES_DATA_URL).json()
heroes_list = {hero["id"]: hero["displayName"] for hero in heroes}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Выбери вражеских героев: /enemy")

# ... остальной код из предыдущего примера ...
