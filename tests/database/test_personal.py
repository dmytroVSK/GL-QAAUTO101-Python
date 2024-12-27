import sqlite3
import pytest


@pytest.mark.database
def test_enable_f_key(db):
    result = db.cursor.execute("PRAGMA foreign_keys").fetchone()[0]
    assert result == 1


@pytest.mark.database
def test_add_not_exist_product_to_orders(db):
    row = db.cursor.execute("""SELECT MAX(id) FROM products""").fetchone()
    product_id = row[0] + 1

    with pytest.raises(sqlite3.IntegrityError):
        db.cursor.execute(
            "INSERT INTO orders (customer_id, product_id) VALUES (?, ?)",
            (1, product_id),
        )


@pytest.mark.database
def test_qnt_orders(db):
    orders = [(1, 1), (1, 2), (1, 3)]
    db.clean_orders_tbl()
    db.cursor.executemany(
        "INSERT INTO orders (customer_id, product_id) VALUES (?, ?)", orders
    )
    db.connection.commit()
    qnt = db.cursor.execute("SELECT COUNT(*) FROM orders;").fetchone()[0]

    assert qnt == len(orders)


@pytest.mark.database
def test_rich_person(db):
    expected = (1, 3)
    orders = [(1, 1), (2, 1), (3, 3), (1, 4), (1, 2)]

    db.clean_orders_tbl()
    db.fill_orders_tbl(orders)
    row = db.cursor.execute(
        """
            SELECT customer_id, COUNT(customer_id) as qnt  
            FROM orders 
            GROUP BY customer_id
            ORDER BY qnt DESC;
            """
    ).fetchone()

    assert row == expected


@pytest.mark.database
def test_popular_product_in_city(db):
    expected = ("Kyiv", "солодка вода", "з цукром", 2)
    orders = [(4, 1), (4, 1), (4, 2), (5, 1), (5, 2)]

    db.clean_orders_tbl()
    db.fill_orders_tbl(orders)
    result = db.cursor.execute(
        """
        SELECT C.city, P.name, P.description, COUNT(P.description) as qnt
        FROM orders AS O 
        INNER JOIN products AS P ON O.product_id = P.id
        INNER JOIN customers AS C ON O.customer_id = C.id
        GROUP BY O.customer_id, O.product_id
        ORDER BY qnt DESC
        LIMIT 1;
        """
    ).fetchall()[0]

    assert result == expected


@pytest.mark.database
def test_not_sold_products(db):
    expected_not_sold = (3, 4, 5)
    orders = [(1, 1), (1, 1), (1, 2)]

    db.clean_orders_tbl()
    db.fill_orders_tbl(orders)
    row = db.cursor.execute(
        """
        SELECT id FROM products
        WHERE id NOT IN (SELECT DISTINCT product_id FROM orders)
        ORDER BY id ASC
        """
    ).fetchall()

    assert (row[0][0], row[1][0], row[2][0]) == expected_not_sold
