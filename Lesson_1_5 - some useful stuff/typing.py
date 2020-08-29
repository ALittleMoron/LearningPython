from typing import (Any, Iterable, List, NewType, NoReturn)


# более удобные переменные
Vector = List[float]
DbName = NewType('DbName', str) #Либо можно просто написать DbName = str


# Далее будут идти фунции-заглушки, которые я не буду вызывать. Просто
# показываю красивую аннотацию типов.
def printing(something:Any) -> NoReturn:
    """ выводит приветствие с переданным аргументом (любым) """
    print('Hello, I am ', something)


def cycle_print(data:Iterable) -> NoReturn:
    """ открывает и записывает в файл данные """
    for enum,it in enumerate(data):
        print(f'data {enum} --- {it}')


def vector_scale(scalar: float, vector: Vector) -> Vector:
    """ увеличивает вектов в scalar раз """
    return [scalar * var for var in vector]


def db_connect(db_name: DbName) -> sqlite.Connection:
    """ создает соединение с базой данных """
    pass


if __name__ == "__main__":
    pass
