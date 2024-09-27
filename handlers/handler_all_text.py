from handlers.handler import Handler
from settings.config import BUTTONS, CATEGORY
from settings.message import MESSAGES
from settings.utility import get_total_coast, get_total_quantity


class HandlerAllText(Handler):
    def __init__(self, bot):
        super().__init__(bot)
        self.step = 0

    def pressed_button_select_product(self, message):
        self.bot.send_message(message.chat.id, 'Категории товаров',
                              reply_markup=self.keyboards.remove_menu())
        self.bot.send_message(message.chat.id, 'Выберите категорию товаров',
                              reply_markup=self.keyboards.category_menu())

    def pressed_button_info(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['info'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.info_menu())

    def pressed_button_settings(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.settings_menu())

    def pressed_button_back(self, message):
        self.bot.send_message(message.chat.id, 'С возвращением назад!',
                              reply_markup=self.keyboards.start_menu())

    def pressed_button_product(self, message, product):
        self.bot.send_message(message.chat.id, f'Категория {BUTTONS[product]}',
                              reply_markup=self.keyboards.set_select_category(CATEGORY[product]))
        self.bot.send_message(message.chat.id, 'Выборка завершена',
                              reply_markup=self.keyboards.category_menu())

    def pressed_button_order(self, message):
        self.step = 0
        count = self.db.select_all_products_id()
        quantity = self.db.select_order_quantity(count[self.step])
        self.send_message_order(count[self.step], quantity, message)

    def pressed_button_up(self, message):
        count = self.db.select_all_products_id()
        quantity_order = self.db.select_order_quantity(count[self.step])
        quantity_product = self.db.select_single_product_quantity(count[self.step])

        if quantity_product > 0:
            quantity_order += 1
            quantity_product -= 1

            self.db.update_order_value(count[self.step], 'quantity', quantity_order)
            self.db.update_product_value(count[self.step], 'quantity', quantity_product)

        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_button_down(self, message):
        count = self.db.select_all_products_id()
        quantity_order = self.db.select_order_quantity(count[self.step])
        quantity_product = self.db.select_single_product_quantity(count[self.step])

        if quantity_order > 0:
            quantity_order -= 1
            quantity_product += 1

            self.db.update_order_value(count[self.step], 'quantity', quantity_order)
            self.db.update_product_value(count[self.step], 'quantity', quantity_order)

        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_button_x(self, message):
        count = self.db.select_all_products_id()

        if count.__len__() > 0:
            quantity_order = self.db.select_order_quantity(count[self.step])
            quantity_product = self.db.select_single_product_quantity(count[self.step])
            quantity_product += quantity_order
            self.db.delete_order(count[self.step])
            self.db.update_product_value(count[self.step], 'quantity', quantity_product)

            if count.__len__() == self.step + 1:
                self.step -= 1

        count = self.db.select_all_products_id()

        if count.__len__() > 0:
            quantity_order = self.db.select_order_quantity(count[self.step])
            self.send_message_order(count[self.step], quantity_order, message)
        else:
            self.bot.send_message(message.chat.id,
                                  MESSAGES['no_orders'],
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.category_menu())

    def pressed_button_previous(self, message):
        if self.step > 0:
            self.step -= 1

        count = self.db.select_all_products_id()
        quantity = self.db.select_order_quantity(count[self.step])

        self.send_message_order(count[self.step], quantity, message)

    def pressed_button_next(self, message):
        if self.step < self.db.count_rows_order() - 1:
            self.step += 1

        count = self.db.select_all_products_id()
        quantity = self.db.select_order_quantity(count[self.step])

        self.send_message_order(count[self.step], quantity, message)

    def pressed_button_button_confirm_order(self, message):
        self.bot.send_message(message.chat.id,
                               MESSAGES['confirm_order'].format(
                                   get_total_coast(self.db),
                                   get_total_quantity(self.db)
                               ),
                               parse_mode='HTML',
                               reply_markup=self.keyboards.category_menu())
        self.db.delete_all_order()

    def send_message_order(self, product_id, quantity, message):
        self.bot.send_message(message.chat.id, MESSAGES['order_number'].format(self.step + 1), parse_mode='HTML')
        self.bot.send_message(message.chat.id,
                              MESSAGES['order'].format(self.db.select_single_product_name(product_id),
                                                       self.db.select_single_product_title(product_id),
                                                       self.db.select_single_product_price(product_id),
                                                       self.db.select_order_quantity(product_id)),
                              parse_mode='HTML',
                              reply_markup=self.keyboards.orders_menu(self.step, quantity))

    def handle(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            if message.text == BUTTONS['SELECT_PRODUCT']:
                self.pressed_button_select_product(message)

            if message.text == BUTTONS['INFO']:
                self.pressed_button_info(message)

            if message.text == BUTTONS['SETTINGS']:
                self.pressed_button_settings(message)

            if message.text == BUTTONS['<<']:
                self.pressed_button_back(message)

            if message.text == BUTTONS['ORDER']:
                if self.db.count_rows_order() > 0:
                    self.pressed_button_order(message)
                else:
                    self.bot.send_message(message.chat.id,
                                          MESSAGES['no_orders'],
                                          parse_mode='HTML',
                                          reply_markup=self.keyboards.category_menu())

            if message.text == BUTTONS['UP']:
                self.pressed_button_up(message)

            if message.text == BUTTONS['DOWN']:
                self.pressed_button_down(message)

            if message.text == BUTTONS['SEMI_FINISHED_PRODUCTS']:
                self.pressed_button_product(message, 'SEMI_FINISHED_PRODUCTS')

            if message.text == BUTTONS['GROCERIES']:
                self.pressed_button_product(message, 'GROCERIES')

            if message.text == BUTTONS['ICE_CREAM']:
                self.pressed_button_product(message, 'ICE_CREAM')

            if message.text == BUTTONS['X']:
                self.pressed_button_x(message)

            if message.text == BUTTONS['NEXT']:
                self.pressed_button_next(message)

            if message.text == BUTTONS['PREVIOUS']:
                self.pressed_button_previous(message)

            if message.text == BUTTONS['CONFIRM_ORDER']:
                self.pressed_button_button_confirm_order(message)

            else:
                self.bot.send_message(message.chat.id, message.text)
