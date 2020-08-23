class Parent1:
    def do_something_1(self):
        print("I'm doing something (1).")


class Parent2:
    def do_something_2(self):
        print("I'm doing something (2).")


class Mixin(Parent1, Parent2):
    def do(self):
        print("Yes, i am")


if __name__ == "__main__":
    a = Mixin()
    a.do()
    a.do_something_1()
    a.do_something_2()
