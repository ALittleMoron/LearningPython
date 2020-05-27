from tkinter import Tk, Frame, Text, Scrollbar
root = Tk()
root.title("практика 6")
root.geometry('500x300+700+300')

fr = Frame(root)
fr.pack(expand = 1, fill='both')

text = Text(fr, width = 30)
text.pack(fill='both', side='left', expand =1)
 
scroll = Scrollbar(fr,command=text.yview)
scroll.pack(side='left', fill='y')

text.config(yscrollcommand=scroll.set)

root.mainloop()