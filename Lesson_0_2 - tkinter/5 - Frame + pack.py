from tkinter import Tk, Label, Frame, Text, Button


root = Tk()
root.title("практика 5")
root.geometry('500x300+700+300')

menu_frame = Frame(root, bg = '#3f383f', width = 50)
main_frame = Frame(root, bg = '#55a594', width = 450)
menu_frame.pack(expand =1, fill='both', side = 'left', anchor='w')
main_frame.pack(expand =1, fill='both', side ='left', anchor='w')

btn = Button(menu_frame, text = 'del', fg = '#fff', bg ='#4f383f')
btn.pack()

text = Text(main_frame, bg = '#55a594', fg='#dacbc1')
text.pack()

root.mainloop()