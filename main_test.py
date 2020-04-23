from main import add, mult

def test_mult():
    assert mult(0, 0) == 0
    assert mult(1, 3) == 3
    assert mult(5, 12) == 60
    assert mult(3, -4) == -12
    assert mult(0, -1) == -1


def test_add():
    assert add(0, 0) == 0
    assert add(1, 3) == 4
    assert add(5, 12) == 17
    assert add(3, -4) == -1
    assert add(0, -1) == -1