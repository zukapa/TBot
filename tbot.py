from telebot import TeleBot

from settings import config
from handlers.handler_main import HandlerMain


class TBot:
    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.handler = HandlerMain(self.bot)

    def start(self):
        self.handler.handle()

    def run_bot(self):
        self.start()
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = TBot()
    bot.run_bot()
