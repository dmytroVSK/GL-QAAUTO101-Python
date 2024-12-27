import pytest


@pytest.mark.database
def test_database_connection(db):
    db.test_connection()


@pytest.mark.database
def test_check_all_users(db):
    users = db.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_sergii(db):
    user: list = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"




@pytest.mark.database
def test_product_insert(db):
    db.insert_product(4, "печиво", "солодке", 30)
    added_cookie = db.select_product_qnt_by_id(4)

    assert added_cookie[0][0] == 30


@pytest.mark.database
def test_product_delete(db):
    db.insert_product(100, "test", "data", 100)
    db.delete_product_by_id(100)
    deleted_product = db.select_product_qnt_by_id(100)

    assert len(deleted_product) == 0


@pytest.mark.database
def test_detailed_orders(db):
    orders = [(1, 1)]
    db.clean_orders_tbl()
    db.fill_orders_tbl(orders)

    orders = db.get_detailed_orders()
    print("Замовлення", orders)

    assert len(orders) == 1

    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_product_qnt_update(db):
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

