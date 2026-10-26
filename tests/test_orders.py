def test_order_status():
    status = "Pending"
    assert status == "Pending"


def test_order_total():
    prices = [5.00, 3.00]
    total = sum(prices)
    assert total == 8.00
