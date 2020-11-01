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