from app.py import sumar
def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(100, 200) == 300
    assert sumar(-5, -5) == -10