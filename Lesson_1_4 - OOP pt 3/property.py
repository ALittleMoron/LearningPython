class XPoint:
    # если я захочу дописать класс, чтобы он умел все то же самое, только ещё и
    # с Y координатой, тогда мне бы пришлось дублировать код, что было бы не в
    # стиле питона...
    # Поэтому ниже более-менее правильный пример, хоть и перегруженный
    def __init__(self, x_point):
        self.__x_point = x_point

    @property
    def x(self):
        return self.__x_point


    @x.setter
    def x(self, new_x):
        self.__x_point = new_x


    @x.deleter
    def x(self):
        del self.__x_point



# более перегруженный вариант. Это можно использовать, но прописывать всё это
# только для того, чтобы можно было удобно менять координаты - вещь спорная.
# В некоторых ситуация может быть полено, но зачастую проще написать отдельный
# метод для этого и всё.
class CoordValue:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:
    coordX = CoordValue()
    coordX = CoordValue()

    def __init__(self, x = 0, y = 0):
        self.coordX = x
        self.coordY = y



if __name__ == "__main__":
    a = Point(25, 25)
    a.coordX = 12
    a.coordY = 2
    print(a.coordX, a.coordY)
