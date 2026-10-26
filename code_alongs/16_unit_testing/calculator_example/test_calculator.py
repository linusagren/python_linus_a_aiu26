from calculator import Calculator

calc = Calculator()

def test_addition():
    num1 = 5
    num2 = 3
    assert calc.add(num1, num2) == num1 + num2

def test_add_negative():
    num1 = -5
    num2 = -3
    assert calc.add(num1, num2) == num1 + num2

def test_subtraction():
    num1 = 5
    num2 = 3
    assert calc.sub(num1, num2) == num1 - num2

def test_negative_subtraction():
    num1 = -5
    num2 = 3
    assert calc.sub(num1, num2) == num1 - num2

def test_multiplication():
    num1 = 6
    num2 = 2
    assert calc.mul(num1, num2) == num1 * num2

def test_negative_multiplication():
    num1 = -6
    num2 = -2
    assert calc.mul(num1, num2) == num1 * num2

def test_division():
    num1 = 4
    num2 = 8
    assert calc.div(num1, num2) == num1 / num2

def test_negative_division():
    num1 = -4
    num2 = -8
    assert calc.div(num1, num2) == num1 / num2

def test_square_root():
    num = 25
    assert calc.sqrt(num) == num**0.5