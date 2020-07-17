# тест алгоритмов сортировки, и их скорость.

from time import monotonic
from random import randint, choice


def benchmark(func):
    """ декоратор, проверяющий время работы функции """
    def wrapper(*args, **kwargs):
        start = monotonic()
        r_v = func(*args, **kwargs)
        end = monotonic()
        print(f'{func.__name__}: {end - start} секунд')
        return r_v
    return wrapper


@benchmark
def default_sorted(seq):
    """ Обертка над функцией sorted() """
    res = sorted(seq)
    return res


@benchmark
def default_sort_method(seq):
    """ Обертка над методом .sort()"""
    res = seq.sort()


@benchmark
def bubble_sort(seq):
    """ Сортировка пузырьком """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True


@benchmark
def selection_sort(seq):
    """ Сортировка выбором """
    for i in range(len(seq)):
        lowest_value_index = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[lowest_value_index]:
                lowest_value_index = j
        seq[i], seq[lowest_value_index] = seq[lowest_value_index], seq[i]


@benchmark
def insertion_sort(seq):
    """ Сортировка вставками """
    for i in range(1, len(seq)):
        item_to_insert = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > item_to_insert:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = item_to_insert


def quick_sort(seq):
    """ Быстрая сортировка """
    if len(seq) <= 1:
        return seq
    else:
        q = choice(seq)
        s_seq, m_seq, e_seq = [], [], []
        for n in seq:
            if n < q:
                s_seq.append(n)
            elif n > q:
                m_seq.append(n)
            else:
                e_seq.append(n)
        return quick_sort(s_seq) + e_seq + quick_sort(m_seq)


@benchmark
def quick_sort_wrapper(seq):
    """ Обертка над quick_sort, чтобы benchmark не выводил лишнюю информацию """
    res = quick_sort(seq)
    return res


if __name__ == "__main__":
    a_1 = default_sorted([randint(-100,100) for _ in range(10000)])
    a_2 = default_sort_method([randint(-100,100) for _ in range(10000)])
    b = bubble_sort([randint(-100,100) for _ in range(10000)])
    c = selection_sort([randint(-100,100) for _ in range(10000)])
    d = insertion_sort([randint(-100,100) for _ in range(10000)])
    e = quick_sort_wrapper([randint(-100,100) for _ in range(10000)])
