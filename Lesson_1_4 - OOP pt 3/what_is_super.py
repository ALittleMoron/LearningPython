import random

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def printer(self):
        print('so, hello my friend!')


    def __str__(self):
        return f'Parent {self.name}, age {self.age}'


class Child(Parent):
    def __init__(self, name, age, random_num):
        super().__init__(name, age)
        self.random_num = random_num


    def printer(self):
        super().printer()
        print('Hola esto burrito izolio. Enato fia avio Salelte.')


    def __str__(self):
        return f'Child with random number {self.random_num}'


if __name__ == "__main__":
    a = Child('Egor', 25, 25)
    a.printer()
    print(a)
