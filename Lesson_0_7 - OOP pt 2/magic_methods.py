class Example():
#    def __new__(cls, ...)    как я понял, лучше не использовать __new__,
#       pass                  либо делать это в крайнем случае. Это не крайний случай


# самый обыкновенный магический метод, кой используется в 99.9999% программ, 
# написанных на python с применением ООП.
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


# Тоже достаточно частый магический метод. Возвращает "читабельный" вид объекта
    def __str__(self):
       return f'Человек с именем {self.first_name} и фамилией {self.last_name}.'


#



# далее 6 примера методов сравнения (== < > != <= >=)
    def __eq__(self, other): 
        # ==, eq = equal - равно
        return self.first_name == other.first_name


    def __lt__(self, other):
        # <, lt = less than - меньше чем
        return len(self.first_name) < len(other.first_name)


    def __gt__(self, other):
        # >, gt = greater than - больше чем
        return len(self.first_name) > len(other.first_name)


    def __ne__(self, other): 
        # !=, ne = not equal - не равно
        return self.first_name != other.first_name


    def __le__(self, other):
        # <=, le = less or equal - меньше или равно
        return len(self.first_name) <= len(other.first_name)


    def __ge__(self, other):
        # >=, ge = greater or equal - больше или равно
        return len(self.first_name) >= len(other.first_name)


# магический метод вызова (Example()), т.е. чтобы объект работал как функция
    def __call__(self, a):
        # тут просто для примера складываются числа
        return sum(a)


if __name__ == "__main__":
    aaa = Example('aaa', 'aaa')
    aaaa = Example('aaaa', 'aaaa')
    a = [25,717,21, -266]
    print(aaa < aaaa)
    print(aaa(a))
    print(aaa)