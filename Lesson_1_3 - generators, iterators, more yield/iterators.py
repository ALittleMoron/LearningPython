Sequence = list


def iter_from_sequence(seq:Sequence):
    """ итератор из последовательности """
    if type(seq) not in (list, set, tuple):
        seq = [1,2,3,4,5]
    return iter(seq)


class SimpleClassIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0


    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


if __name__ == "__main__":
    a = iter_from_sequence([25,12,52,25,2,3,5,678, 1.2])
    print(next(a))
    print(next(a))
    del(a)
    a = SimpleClassIterator(10)
    print(next(a), next(a), next(a))
    print(next(a))
