import os

import telegram

tg_token = os.environ["TG_TOKEN"]

tg_bot = telegram.Bot(token=tg_token)
tg_bot.send_message(chat_id=-1002232809574, text="Тестовое сообщение")
