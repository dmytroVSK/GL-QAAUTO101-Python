import sqlite3


class DBHandler:

    @classmethod
    def _script_execute_and_commit(cls, connection, sql_script):
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()

    @classmethod
    def fetchall(cls, db_path, sql_script):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_script)
            rows = cursor.fetchall()
            return rows

    @classmethod
    def run_queries(cls, db_path, sql_scripts: list):
        with sqlite3.connect(db_path) as conn:

            for script in sql_scripts:
                cls._script_execute_and_commit(conn, script)
                # print('Script executed !!!')


    # sql queries

    CREATE_PRODUCTS_TBL_SQL = '''
        CREATE TABLE IF NOT EXISTS products
        (id integer PRIMARY KEY, name TEXT,description TEXT,quantity INTEGER);
        '''
    FILL_PRODUCTS_TBL_SQL = '''
        INSERT INTO products (id, name, description, quantity)
        VALUES
        (1, 'солодка вода',	'з цукром', 10),
        (2, 'солодка вода', 'з цукрозамінником', 10);
        '''
    CREATE_CUSTOMERS_TBL_SQL = '''
        CREATE TABLE IF NOT EXISTS customers 
        (id INTEGER PRIMARY KEY, name TEXT, address TEXT, city TEXT, postalCode TEXT, country TEXT);
        '''
    FILL_CUSTOMERS_TBL_SQL = '''
        INSERT INTO customers (id, name, address, city, postalCode, country) 
        VALUES 
        (1, 'Sergii', 'Maydan Nezalezhnosti 1', 'Kyiv' , '3127', 'Ukraine'),
        (2, 'Stepan', 'Stepana Bandery str 2', 'Kyiv', '2055', 'Ukraine');
        '''
    CREATE_ORDERS_TBL_SQL = '''
        CREATE TABLE orders (
            id integer PRIMARY KEY,
            customer_id integer,
            product_id integer,
            order_date datetime,
            FOREIGN KEY(customer_id) REFERENCES customers(id),
            FOREIGN KEY(product_id) REFERENCES orders(id)
        );
        '''
    FILL_ORDERS_TBL_SQL = '''
        INSERT INTO orders (id, customer_id, product_id, order_date)
        VALUES 
        (1, 1, 1, '12:22:23')
        '''

