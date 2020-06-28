from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass #just checking dataclass with ABC. Useless thing in this code.
class Hello(ABC):
    a:str = 'I am'
    b:int = 25

    @abstractmethod
    def show(self):
        print(f'Hello, {self.a} {self.b}!') 


class WhoAreYou(Hello):
    def show(self):
        super().show()
        print('Just a number, but i have a dream!')


# a = Hello() #Can't instantiate abstract class Hello with abstract methods show
b = WhoAreYou() # b was created without error
b.show() # Its alive!
