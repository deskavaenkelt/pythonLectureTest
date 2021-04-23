import Calculator


def test_addition():
    assert 4 == Calculator.addition(2, 2)
    assert 10 == Calculator.addition(5, 5)
    assert 0 == Calculator.addition(0, 0)
    assert 10 != Calculator.addition(6, 5)


def test_subtraction():
    assert 4 == Calculator.subtraction(6, 2)
    assert 2 == Calculator.subtraction(5, 3)
    assert 0 == Calculator.subtraction(0, 0)
    assert 10 != Calculator.subtraction(6, 5)


def test_multiply():
    assert 12 == Calculator.multiply(6, 2)
    assert 15 == Calculator.multiply(5, 3)
    assert 0 == Calculator.multiply(0, 0)
    assert 10 != Calculator.multiply(6, 5)
