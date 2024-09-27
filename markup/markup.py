from telebot.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup,
                           InlineKeyboardButton)

from settings.config import BUTTONS
from data_base.dbalchemy import DBManager


class Keyboards:
    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    def set_button(self, name, step=0, quantity=0):
        if name == 'AMOUNT_ORDER':
            BUTTONS['AMOUNT_ORDER'] = 'Товары в заказе: {} {} {}'.format( step + 1, ' из ', str(self.DB.count_rows_order()))

        if name == 'AMOUNT_PRODUCT':
            BUTTONS['AMOUNT_PRODUCT'] = 'Количество в заказе: {}'.format(quantity)

        return KeyboardButton(BUTTONS[name])

    def start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)

        button_select_product = self.set_button('SELECT_PRODUCT')
        button_info = self.set_button('INFO')
        button_settings = self.set_button('SETTINGS')

        self.markup.row(button_select_product)
        self.markup.row(button_info, button_settings)

        return self.markup

    def info_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)

        button_back = self.set_button('<<')
        self.markup.row(button_back)

        return self.markup

    def settings_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)

        button_back = self.set_button('<<')
        self.markup.row(button_back)

        return self.markup

    def remove_menu(self):
        return ReplyKeyboardRemove()

    def category_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)

        self.markup.add(self.set_button('SEMI_FINISHED_PRODUCTS'))
        self.markup.add(self.set_button('GROCERIES'))
        self.markup.add(self.set_button('ICE_CREAM'))
        self.markup.row(self.set_button('<<'), self.set_button('ORDER'))

        return self.markup

    def orders_menu(self, step, quantity):
        self.markup = ReplyKeyboardMarkup(True, True)

        button_delete_order = self.set_button('X', step, quantity)
        button_down_order = self.set_button('DOWN', step, quantity)
        button_up_order = self.set_button('UP', step, quantity)
        button_amount_product = self.set_button('AMOUNT_PRODUCT', step, quantity)

        button_back_step = self.set_button('PREVIOUS', step, quantity)
        button_next_step = self.set_button('NEXT', step, quantity)
        button_amount_order = self.set_button('AMOUNT_ORDER', step, quantity)

        button_confirm_order = self.set_button('CONFIRM_ORDER', step, quantity)
        button_back = self.set_button('<<', step, quantity)

        self.markup.row(button_delete_order, button_down_order, button_up_order, button_amount_product)
        self.markup.row(button_back_step, button_next_step, button_amount_order)
        self.markup.row(button_back, button_confirm_order)

        return self.markup

    def set_inline_button(self, name):
        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    def set_select_category(self, category):
        self.markup = InlineKeyboardMarkup(row_width=1)

        for category_DB in self.DB.select_all_products_category(category):
            self.markup.add(self.set_inline_button(category_DB))

        return self.markup
