def convert_list(list_convert):
    return [item[0] for item in list_convert]

def total_coast(list_quantity, list_price):
    order_total_coast = 0

    for index, price in enumerate(list_price):
        order_total_coast += list_quantity[index] * list_price[index]

    return order_total_coast

def total_quantity(list_quantity):
    order_total_quantity = 0

    for quantity in list_quantity:
        order_total_quantity += quantity

    return order_total_quantity

def get_total_coast(db):
    all_products_id = db.select_all_products_id()
    all_price = [db.select_single_product_price(product_id) for product_id in all_products_id]
    all_quantity = [db.select_order_quantity(product_id) for product_id in all_products_id]

    return total_coast(all_quantity, all_price)

def get_total_quantity(db):
    all_products_id = db.select_all_products_id()
    all_quantity = [db.select_order_quantity(product_id) for product_id in all_products_id]

    return total_quantity(all_quantity)
