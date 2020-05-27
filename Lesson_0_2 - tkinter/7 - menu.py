from tkinter import Tk, Menu, Frame
root = Tk()
root.title("практика 7")
root.geometry('500x300+700+300')

fr = Frame(root)
fr.pack(expand = 1, fill='both')
mainmenu = Menu(root) 
root.config(menu=mainmenu) 
 
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")
 
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")
 
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)
root.mainloop()