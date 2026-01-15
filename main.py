import telebot
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
bot.send_message(
message.chat.id,
"✅ Miles/Payback Radar aktiv\n🇩🇪 Deutschland\n🔔 Bot läuft"
)

@bot.message_handler(commands=["status"])
def status(message):
bot.send_message(message.chat.id, "🟢 Status: aktiv")

while True:
try:
bot.polling(non_stop=True)
except:
time.sleep(5)
