import os
from telegram.ext import (
    Application,
    CommandHandler as CM,
)

from bot.commands import CommandHandler
from bot.handler import EventHandler


class Bot:
    def __init__(self):
        self.TOKEN = os.environ.get('TELEGRAM_TOKEN')
        if not self.TOKEN:
            raise ValueError('Telegram token not found')
        self.app = Application.builder().token(self.TOKEN).build()
        self.commands = CommandHandler(self.app.bot)
        self.handler = EventHandler(self.commands.notify)
        self.app.add_handlers([
            CM('start',self.commands.start),
            CM('enable',self.commands.enable),
            CM('disable',self.commands.disable)
        ])
    def start(self):
        self.app.run_polling()