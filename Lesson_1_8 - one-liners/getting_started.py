"""
По заветам Питоновского Дзена "Простое лучше, чем сложное".
А что может быть проще фунции, написанной в 1 строчку с одним return'ом?
Конечно, далеко не всегда можно писать в таком стиле, но тех возможносте,
которые дает Python, на 99% хватает для повседневного программирования.
"""


# list comprehensions:
def list_of_numbers(range_num: int) -> list:
    """ принимает число, возвращает list comprehensions из чисел от 0 до range_num+1. """
    return [x for x in range(range_num+1)]


def list_of_odd_numbers(range_num: int) -> list:
    """ принимает число, возвращает list comprehensions из нечетных чисел от 0 до range_num+1. """
    return [x for x in range(range_num+1) if x % 2]


def from_text_to_lines(text) -> list:
    """ принимает многострочный текст, возвращает строки из него. """
    return [line.strip() for line in text.split('\n')]



"""
При этом те же функции можно написать и при помощи lambda, но это, я так понял,
не очень поощряется в python-среде, и анонимные функции лучше оставить на всякие
map, filter, functools.reduce и так далее. 

Есть ещё 1 способ улучшить функции выше: написать то же самое, но в круглых скобках,
т.е. написать one-line generator.
"""


# (map or filter) + lambda:
def squared_numbers(range_num:int) -> map:
    """ возвращает map-объект последовательности чисел от 0 до range_num+1, возведенные в степень 
    Аналог - (x**2 for x in range(range_num+1)). Это даже проще, чем map, но я ничего серьезнее не придумал.
    """
    return map(lambda x: x**2, (y for y in range(range_num+1))) 


def odd_filtered_numbers(range_num:int) -> filter:
    """ возвращает filter-объект последовательности нечетных чисел от 0 до range_num+1 
    Аналог - (x for x in range(range_num+1) if x%2). Более серьезную реализацию тоже не придумал.
    """
    return filter(lambda x: x%2, (y for y in range(range_num+1)))



"""
Также можно создавать и другие последовательности как при list comprehensions.
Например, словари, множества и даже словари словарей, списки списков и т.д.
"""


# dict comprehensions and list of lists:
def letter_count(string:str) -> dict:
    """ возвращает словарь с "ключ-значением" в виде "символ-число символов в строке". """
    return {letter: string.count(letter) for letter in string}


def from_text_to_lines_to_words(text:str) -> list:
    """ тот же from_text_to_lines, но с разделением строк на слова. """
    return [line.strip().split() for line in text.split('\n')]


def list_of_lists(range_num) -> list:
    """ возвращает список из range_num**2 списков перестановки 2-х чисел от 0 до range_num+1 """
    return [[x,y] for x in range(range_num+1) for y in range(range_num+1)]



"""
Хороший вариант - это проход не по объекту range, а по переданным в качестве аргумента функции спискам.
Но что если нужно пройтись по списку скисков? Как, например, создать из списка списков 1 большой список
со всеми элементами [][x]? Оказывается, достаточно просто это можно сделать также в 1 строку.
"""


# cycle for sequence
def filter_of_odd_numbers(seq:list) -> list:
    """ такой же фильтр, что и выше, но без функции filter и без range. """
    return [x for x in seq if x%2]


def from_list_of_lists_to_list(seq:list) -> list:
    """ раскрывает список списков в обычный список. """
    return [x for y in seq for x in y]



"""
Неплохой способ работы с такими только что созданными списками, словарями или множествами - это
отправка их в качестве аргумента для функций и методов map, filter, join и похожих.
При это с какого-то момента такие вложения друг в друга становятся на столько сложными, что
понять, что строка делает, становится достаточно сложно.

Пример: 
def ip_to_int32(ip):
    return sum([2**e for e, z in enumerate(str(''.join([('0' * (8 - len(y))) + y for y in [bin(int(x))[2:] for x in ip.split('.')]]))[::-1]) if z == '1'])

^ тут функция занимается тем, что принимает строку IP, переводит каждый элемент в двоичную систему в 8 знаками (1 = 00000001), объединяет элементы в одно
большое двочное число и переводит его обратно в десятичное. Я долго всматривался, чтобы понять, в каком порядке и что она делает. При этом повторить такое
проблематично. Это превращается уже в написание регулярных выражений, что, думаю, не есть хорошо, так как читаемость кода падает в разы.
"""


def sum_of_odd_numbers(range_num: int) -> int:
    """ возвращает сумму нечетных чисел от 0 до range_num+1 """
    return sum([x for x in range(range_num+1) if x%2])


def odd_numbers_to_string_with_sep(range_num:int) -> str:
    """ возвращает конкатинированную строку из последовательности нечетных чисел от 0 до range_num+1
    с сепаратором в виде '__'
     """
    return '__'.join([str(x) for x in range(range_num+1) if x%2])


if __name__ == "__main__":
    text = """
        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!
    """
    print(list_of_numbers(5), list_of_odd_numbers(5), from_text_to_lines(text), sep='\n', end= '\n\n')
    print(list(squared_numbers(5)), list(odd_filtered_numbers(5)), sep='\n', end='\n\n')
    print(letter_count('string for count.'), from_text_to_lines_to_words(text), list_of_lists(5), sep='\n', end='\n\n')
    print(filter_of_odd_numbers([1, 2, 13, 66621, 125, 12, 52, 345]), from_list_of_lists_to_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), sep='\n', end='\n\n')
    print(sum_of_odd_numbers(5), odd_numbers_to_string_with_sep(5), sep='\n', end='\n\n')