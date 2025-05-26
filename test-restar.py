from app.py import restar
def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 0) == 0
    assert restar(-1, -1) == 0
    assert restar(10, 5) == 5
    assert restar(100, 200) == -100