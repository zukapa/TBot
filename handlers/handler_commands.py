from handlers.handler import Handler


class HandlerCommands(Handler):
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_button_start(self, message):
        self.bot.send_message(message.chat.id,
                              f'Привет {message.from_user.first_name}! '
                              f'Введите команду для начала работы.',
                              reply_markup=self.keyboards.start_menu())

    def handle(self):
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                self.pressed_button_start(message)
