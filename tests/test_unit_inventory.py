import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.inventory import calculate_total_price

def test_calculate_total_price():
    assert calculate_total_price(10000, 2) == 20000
    assert calculate_total_price(5000, 0) == 0
