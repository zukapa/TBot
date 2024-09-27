from settings.config import BUTTONS, VERSION, AUTHOR

info = """
<b>Добро пожаловать!</b>

Это приложение предназначено для заказа товаров без взаимодействия с сайтом.
"""

settings = """
<b>Основные кнопки управления:</b>

<i>Навигация:</i>

<b>{} - </b><i>назад</i>
<b>{} - </b><i>вперед</i>
<b>{} - </b><i>увеличить</i>
<b>{} - </b><i>уменьшить</i>
<b>{} - </b><i>следующий</i>
<b>{} - </b><i>предыдущий</i>

<i>Специальные кнопки:</i>

<b>{} - </b><i>удалить</i>
<b>{} - </b><i>заказ</i>
<b>{} - </b><i>оформить заказ</i>

<b>Общая информация:</b>

<b>версия программы: - </b><i>{}</i>
<b>разработчик: - </b><i>{}</i>

<b>{} разработчик бота</b>
""".format(
    BUTTONS['<<'],
    BUTTONS['>>'],
    BUTTONS['UP'],
    BUTTONS['DOWN'],
    BUTTONS['NEXT'],
    BUTTONS['PREVIOUS'],
    BUTTONS['X'],
    BUTTONS['ORDER'],
    BUTTONS['CONFIRM_ORDER'],
    VERSION,
    AUTHOR,
    BUTTONS['COPYRIGHT'],
)

add_product_order = """
В заказ добавлен товар:

{}
{}
Цена: {} руб.

На складе осталось {} ед.
"""

order = """
<i>Наименование товара:</i> <b>{}</b>
<i>Производитель:</i> <b>{}</b>
<i>Цена:</i> <b>{} руб. за 1 ед.</b>
<i>Количество в заказе:</i> <b>{} ед.</b>
"""

order_number = """
<b>Номер товара в заказе: </b> <i>{}</i>
"""

no_orders = """
<b>Заказов нет.</b>
"""

confirm_order = """
<b>Заказ принят.</b>

<i>Общая стоимость заказа: </i> <b>{} руб.</b>
<i>Общее количество товаров: </i> <b>{} ед.</b>
"""

MESSAGES = {
    'info': info,
    'add_product_order': add_product_order,
    'order': order,
    'order_number': order_number,
    'no_orders': no_orders,
    'confirm_order': confirm_order,
    'settings': settings
}
