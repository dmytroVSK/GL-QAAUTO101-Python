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

    CREATE_PRODUCTS_TBL_SQL = """
        CREATE TABLE IF NOT EXISTS products (
            id integer PRIMARY KEY AUTOINCREMENT, 
            name TEXT,
            description TEXT,
            quantity INTEGER DEFAULT 0
        );
        """
    FILL_PRODUCTS_TBL_SQL = """
        INSERT INTO products (name, description, quantity)
        VALUES
        ('солодка вода',	'з цукром', 10),
        ('солодка вода', 'з цукрозамінником', 15),
        ('солодка вода', 'з соком', 30),
        ('узвар', 'з цукром', 50),
        ('узвар', 'з цукрозамінником', 5);
        """
    CREATE_CUSTOMERS_TBL_SQL = """
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            address TEXT, 
            city TEXT, 
            postalCode TEXT DEFAULT '0000', 
            country TEXT DEFAULT 'Ukraine'
        );
        """
    FILL_CUSTOMERS_TBL_SQL = """
        INSERT INTO customers (name, address, city, postalCode, country) 
        VALUES 
        ('Sergii', 'Maydan Nezalezhnosti 1', 'Kyiv' , '3127', 'Ukraine'),
        ('Stepan', 'Stepana Bandery str 2', 'Kyiv', '2055', 'Ukraine'),
        ('Mykola', 'Nema moskalya 10', 'Lviv', '2055', 'Ukraine'),
        ('Vasyl', 'Stepana Bandery str 10', 'Kyiv', '2055', 'Ukraine'),
        ('John', 'Stepana Bandery str 2', 'New York', '0000', 'USA');
        """
    CREATE_ORDERS_TBL_SQL = """
        CREATE TABLE IF NOT EXISTS orders (
            id integer PRIMARY KEY AUTOINCREMENT,
            customer_id integer,
            product_id integer,
            order_date datetime DEFAULT CURRENT_DATE,
            FOREIGN KEY(customer_id) REFERENCES customers(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        );
        """
    FILL_ORDERS_TBL_SQL = """
        INSERT INTO orders (customer_id, product_id)
        VALUES 
        (1, 4),
        (2, 4),
        (4, 3),
        (3, 4),
        (5, 1),
        (5, 2),
        (1, 5);
        """
