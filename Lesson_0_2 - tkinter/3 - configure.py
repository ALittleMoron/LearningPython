from tkinter import Tk, Label


root = Tk()
root.title("практика 3")
root.geometry('500x300+700+300')

lbl_1 = Label(root, text = 'Hello, World!')
lbl_1.pack()

lbl_2 = Label(root, text = "Hello, World!" , font=('Times New Roman', 20, 'bold'))
lbl_2.pack()

lbl_3 = Label(root, text = "Hello, World!"  , bg = 'green', fg ='red', font=('Comic Sans MS', 30, 'italic'))
lbl_3.pack()

lbl_4 = Label(root, text = "Hello, World!"  , bg = 'yellow', fg ='blue', font=('Arial', 40))
lbl_4.pack()


lbl_1.config(bg ='green')
lbl_2['bg'] = 'green'
lbl_3.configure(fg = 'gray')
lbl_4['fg'] = 'purple'

root.mainloop()