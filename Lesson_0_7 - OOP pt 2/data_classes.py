from dataclasses import dataclass, field
from random import randint
from typing import List

@dataclass
class Human:
    age: int = 0
    gender: str = 'man'

@dataclass()
class Person(Human):
    name: str = 'John Smith'
    
    def __post_init__(self):
        self.money_bag: int = randint(0, 1000)

a = Person(14, 'woman', 'Wilma Smith')
print(a, Person, a.age, a.gender, a.name, a.money_bag)




def get_random_marks():
    return [randint(0,10) for _ in range(10)]

@dataclass
class Mass:
    ms: List[int] = field(default_factory = get_random_marks)

b = Mass()
print(b, Mass, b.ms)




@dataclass(order=True)
class Num:
    name:int = field(compare=False, repr=True)
    num:int = field(compare=True, repr=False)

c = Num('3', 3)
d = Num('4', 4)
print(c < d, c > d, c, d, Num)