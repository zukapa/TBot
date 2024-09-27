import os

from emoji import emojize

TOKEN = '7892240722:AAFc1vMYSHsuxrhC9aOX_wpGnl1fEnbUVgY'
DB_NAME = 'products.db'
VERSION = '0.1'
AUTHOR = 'Human'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:///' + BASE_DIR, DB_NAME)

COUNT = 0

BUTTONS = {
    'SELECT_PRODUCT': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize(':gear: Настройки'),
    'SEMI_FINISHED_PRODUCTS': emojize(':ice: Полуфабрикаты'),
    'GROCERIES': emojize(':candy: Бакалея'),
    'ICE_CREAM': emojize(':ice_cream: Мороженое'),
    '<<': emojize(':left_arrow: Назад'),
    '>>': emojize(':right_arrow:'),
    'NEXT': emojize(':play_button: Следующий товар'),
    'PREVIOUS': emojize(':reverse_button: Предыдущий товар'),
    'ORDER': emojize(':check_mark: Заказ'),
    'X': emojize(':multiply: Удалить товар'),
    'UP': emojize(':up_arrow: Добавить товар'),
    'DOWN': emojize(':down_arrow: Убрать товар'),
    'AMOUNT_PRODUCT': '',
    'AMOUNT_ORDER': '',
    'CONFIRM_ORDER': emojize(':OK_button: Подтвердить заказ'),
    'COPYRIGHT': emojize(':copyright:'),
}

CATEGORY = {
    'SEMI_FINISHED_PRODUCTS': 3,
    'GROCERIES': 2,
    'ICE_CREAM': 1
}

COMMANDS = {
    'START': 'start',
    'HELP': 'help'
}
