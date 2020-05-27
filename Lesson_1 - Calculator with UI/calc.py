from tkinter import Tk, Button, Label, Frame

class Main:
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        pass



if __name__ == "__main__":
    root = Tk()
    root.title("Калькулятор")
    root.geometry('300x400+300+200')
    root.resizable(0,0)
    app = Main(root)

    btn_list  = [
        '7', '8', '9',
        '4', '5', '6',
        '1', '2', '3',
        '0'
    ]

    root.mainloop()