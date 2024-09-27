import sqlite3
from settings.config import DB_NAME

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS category (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR NOT NULL,
is_active BOOLEAN NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR NOT NULL,
title VARCHAR NOT NULL,
price FLOAT NOT NULL,
quantity INTEGER NOT NULL,
is_active BOOLEAN NOT NULL,
category_id INTEGER NOT NULL,
FOREIGN KEY (category_id) REFERENCES category (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS discount (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
product_id INTEGER NOT NULL,
discount INTEGER NOT NULL,
FOREIGN KEY (product_id) REFERENCES product (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
quantity INTEGER NOT NULL,
date DATETIME NOT NULL,
product_id INTEGER NOT NULL,
user_id INTEGER NOT NULL,
FOREIGN KEY (product_id) REFERENCES product (id)
)
''')

connection.commit()
connection.close()
