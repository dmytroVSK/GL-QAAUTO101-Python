import sqlite3
import pytest


@pytest.mark.database
def test_product_qnt_update(db):
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_add_not_exist_product_to_orders(db, pause):
    db.cursor.execute("""SELECT MAX(id) FROM products""")
    row = db.cursor.fetchone()

    with pytest.raises(sqlite3.IntegrityError):
        db.cursor.execute(
            "INSERT INTO orders (id, customer_id, product_id, order_date) VALUES (1, 1, ?, '12:22:23')",
            (row[0] + 1,),
        )


@pytest.mark.database
def test_new(db):
    pass



