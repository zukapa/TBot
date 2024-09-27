from handlers.handler import Handler
from settings.message import MESSAGES


class HandlerInlineQuery(Handler):
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_button_product(self, call, code):
        self.db._add_orders(1, code, 1)

        self.bot.answer_callback_query(
            call.id,
            MESSAGES['add_product_order'].format(
                self.db.select_single_product_name(code),
                self.db.select_single_product_title(code),
                self.db.select_single_product_price(code),
                self.db.select_single_product_quantity(code)
            ),
            show_alert=True
        )

    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            code = call.data
            if code.isdigit():
                code = int(code)

            self.pressed_button_product(call, code)
