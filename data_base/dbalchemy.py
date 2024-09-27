from os import path
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base.dbcore import Base

from settings.config import DATABASE
from settings.utility import convert_list
from models.product import Product
from models.order import Order

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)

        return cls.__instance


class DBManager(metaclass=Singleton):
    def __init__(self):
        self.engine = create_engine(DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        if not path.isfile(DATABASE):
            Base.metadata.create_all(self.engine)

    def close(self):
        self._session.close()

    def select_all_products_category(self, category_id):
        result = self._session.query(Product).filter_by(category_id=category_id).all()
        self.close()

        return result

    def _add_orders(self, quantity, product_id, user_id):
        id_products_all = self.select_all_products_id()

        if product_id in id_products_all:
            quantity_order = self.select_order_quantity(product_id)
            quantity_order += 1
            self.update_order_value(product_id, 'quantity', quantity_order)

            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)

            return
        else:
            order = Order(quantity=quantity, product_id=product_id, user_id=user_id, date=datetime.now())
            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)

        self._session.add(order)
        self._session.commit()
        self.close()

    def select_all_products_id(self):
        result = self._session.query(Order.product_id).all()
        self.close()

        return convert_list(result)

    def select_order_quantity(self, product_id):
        result = self._session.query(Order.quantity).filter_by(product_id=product_id).one()
        self.close()

        return result.quantity

    def select_single_product_quantity(self, product_id):
        result = self._session.query(Product.quantity).filter_by(id=product_id).one()
        self.close()

        return result.quantity

    def select_single_product_name(self, product_id):
        result = self._session.query(Product.name).filter_by(id=product_id).one()
        self.close()

        return result.name

    def select_single_product_title(self, product_id):
        result = self._session.query(Product.title).filter_by(id=product_id).one()
        self.close()

        return result.title

    def select_single_product_price(self, product_id):
        result = self._session.query(Product.price).filter_by(id=product_id).one()
        self.close()

        return result.price

    def select_single_product_category(self, product_id):
        result = self._session.query(Product.category_id).filter_by(id=product_id).one()
        self.close()

        return result

    def count_rows_order(self):
        result = self._session.query(Order).count()
        self.close()

        return result

    def update_order_value(self, product_id, name, value):
        self._session.query(Order).filter_by(product_id=product_id).update({name: value})
        self._session.commit()
        self.close()

    def update_product_value(self, product_id, name, value):
        self._session.query(Product).filter_by(id=product_id).update({name: value})
        self._session.commit()
        self.close()

    def delete_order(self, product_id):
        self._session.query(Order).filter_by(product_id=product_id).delete()
        self._session.commit()
        self.close()

    def delete_all_order(self):
        all_id_orders = self.select_all_orders_id()

        for id_order in all_id_orders:
            self._session.query(Order).filter_by(id=id_order).delete()
            self._session.commit()

        self.close()

    def select_all_orders_id(self):
        result = self._session.query(Order.id).all()
        self.close()

        return convert_list(result)
