class LazyCalculator():
    @staticmethod
    def add(x, y):
        return x + y


    @staticmethod
    def dl(x, y):
        return x - y


    @staticmethod
    def mult(x, y):
        return x * y


    @staticmethod
    def div(x, y):
        return x / y if y !=0 else 0


class MathWithParams():
    @staticmethod
    def some_math_function(a,b,c):
        return a + b * c
