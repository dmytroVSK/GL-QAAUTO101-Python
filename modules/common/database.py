import sqlite3
from pathlib import Path


class Database:

    def __init__(self, sqlite_db_name):
        self.connection = sqlite3.connect(sqlite_db_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.close()

    def close(self):
        if self.connection:
            self.connection.close()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database version is : {record[0][0]}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = (
            "SELECT address, city, postalCode, country FROM customers WHERE name = ?;"
        )
        self.cursor.execute(query, (name,))
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = "UPDATE products SET quantity = ? WHERE id = ?;"
        self.cursor.execute(query, (qnt, product_id))
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = "SELECT quantity FROM products WHERE id = ?;"
        self.cursor.execute(query, (product_id,))
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = """INSERT OR REPLACE INTO products 
                (id, name, description, quantity) 
                VALUES 
                (?, ?, ?, ?);
                """

        self.cursor.execute(query, (product_id, name, description, qnt))
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = "DELETE FROM products WHERE id = ?;"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()

    def get_detailed_orders(self):
        query = """SELECT orders.id, customers.name, products.name,
                          products.description, orders.order_date
                   FROM orders
                   JOIN customers ON orders.customer_id = customers.id
                   JOIN products ON orders.product_id = products.id;
                   """
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
