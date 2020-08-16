import random, pytest
from some_code import LazyCalculator, MathWithParams


def test_add():
    calc = LazyCalculator()
    a, b = random.randint(-20, 20), random.randint(-20,20)
    assert calc.add(a, b) == a+b


def test_dl():
    calc = LazyCalculator()
    a, b = random.randint(-20, 20), random.randint(-20,20)
    assert calc.dl(a, b) == a - b


def test_mult():
    calc = LazyCalculator()
    a, b = random.randint(-20, 20), random.randint(-20,20)
    assert calc.mult(a, b) == a * b


def test_div():
    calc = LazyCalculator()
    a, b = random.randint(-20, 20), random.randint(-20,20)
    assert calc.div(a, b) == a / b


class TestLikeProfessional:
    @pytest.mark.parametrize("args, result", [
            pytest.param((1,4,2), 9,),
            pytest.param((25,1,2), 27,),

    ])
    def test_isinstanse(self, args, result):
        assert MathWithParams.some_math_function(*args) == result


