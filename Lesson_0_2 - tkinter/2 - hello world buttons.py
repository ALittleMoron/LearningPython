from tkinter import Tk, Label, Button

def lbl_hello():
    print("Hello")


root = Tk()
root.title("практика 2")
root.geometry('500x300+700+300')

lbl_3 = Label(root, text = "Hello, World!"  , bg = 'green', fg ='red', font=('Comic Sans MS', 30, 'italic'))
lbl_3.pack()

btn_1 = Button(text='say hello', command=lbl_hello)
btn_1.pack()

root.mainloop()