from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from models.product import Product
from data_base.dbcore import Base


class Discount(Base):
    __tablename__ = 'discount'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    discount = Column(Integer)

    product = relationship(Product, backref=backref('discount',
                                                    cascade='all, delete'))
