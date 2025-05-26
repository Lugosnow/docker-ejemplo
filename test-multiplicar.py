from app.py import multiplicar
def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 5) == 0
    assert multiplicar(100, 200) == 20000
    assert multiplicar(-5, -5) == 25
    assert multiplicar(0, 0) == 0
    assert multiplicar(1, 1) == 1