Sequence = list # или tuple, или set


def simple_counter(num:int):
    """ генератор-счетчик от 0 до num """
    if type(num) != int:
        num = 5
    for i in range(num):
        yield i


def seq_to_generator(seq:Sequence):
    """ генератор из последовательности (list, set, tuple) """
    if type(seq) not in (list, tuple, set):
        seq = [1,2,3,4,5]
    return (x for x in seq)


class SimpleClassGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        while self.count < self.limit:
            yield self.count
            self.count += 1


if __name__ == "__main__":
    # код не на столько сложный, чтобы писать отдельный pytest для всего этого
    print('simple_counter тест:')
    a = simple_counter(25)
    print(a, type(a), sum(a), sep = '  -----  ')
    for num in simple_counter(5):
        print(num)
    del(a)

    print('\nseq_to_generator тест:')
    a = seq_to_generator([25, 75, 'sadboy', ('yakuza zero', 'doom 3', 222)])
    print(a, type(a), sep = '  -----  ')
    for num in a:
        print(num, type(num), sep = '  -----  ')
    del(a)

    print('\nSimpleClassGenerator тест:')
    a = SimpleClassGenerator(20)
    print(a, type(a), sum(a), sep = '  -----  ')

