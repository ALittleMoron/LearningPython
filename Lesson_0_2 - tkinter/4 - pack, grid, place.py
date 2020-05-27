from tkinter import Tk, Label, Button, Entry, ttk, Spinbox


root = Tk()
root.title("практика 4")
root.geometry('500x300+700+300')

#pack():
# Button(text = '1', bg="#028603", height = 2, width = 6, fg='#c223b2').pack(side='left')
# Button(text = '1', bg="#028603", height = 2, width = 6, fg='#c223b2').pack(side='left')
# Button(text = '1', bg="#028603", height = 2, width = 6, fg='#c223b2').pack(side='left')
# Button(text = '2', bg="#cff210", height = 2, width = 6, fg='#172c6c').pack(side='right')
# Button(text = '2', bg="#cff210", height = 2, width = 6, fg='#172c6c').pack(side='right')
# Button(text = '2', bg="#cff210", height = 2, width = 6, fg='#172c6c').pack(side='right')
# Button(text = '3', bg="#651ca7", height = 2, width = 6, fg='#f11daf').pack(side='top')
# Button(text = '3', bg="#651ca7", height = 2, width = 6, fg='#f11daf').pack(side='top')
# Button(text = '3', bg="#651ca7", height = 2, width = 6, fg='#f11daf').pack(side='top')
# Button(text = '4', bg="#973d66", height = 2, width = 6, fg='#b9f754').pack(side='bottom')
# Button(text = '4', bg="#973d66", height = 2, width = 6, fg='#b9f754').pack(side='bottom')
# Button(text = '4', bg="#973d66", height = 2, width = 6, fg='#b9f754').pack(side='bottom')
# Button(text= '1', bg='lightblue', height = 3, width = 9).pack(expand=1, fill='x', anchor ='n')
# Button(text= '1', bg='lightblue', height = 3, width = 9).pack(fill='x')
# Button(text= '1', bg='lightblue', height = 3, width = 9).pack(fill='x')
# Button(text= '1', bg='lightblue', height = 3, width = 9).pack(fill='x')
# Button(text= '1', bg='lightblue', height = 3, width = 9).pack(fill='x')
# Button(text= '1', bg='lightblue', height = 3, width = 9).pack(expand=1, fill='x')
# Button(text= '1', bg='lightblue', height = 3, width = 9).pack(expand=1, fill='x', anchor ='s')


#grid():
# Button(text = '1', bg="#028603", height = 2, width = 6, fg='#c223b2').grid(row=0, column=0)
# Button(text = '1', bg="#028603", height = 2, width = 6, fg='#c223b2').grid(row=0, column=3)
# Button(text = '1', bg="#028603", height = 2, width = 6, fg='#c223b2').grid(row=0, column=4)
# Button(text = '2', bg="#cff210", height = 2, width = 6, fg='#172c6c').grid(row=1, column=0)
# Button(text = '2', bg="#cff210", height = 2, width = 6, fg='#172c6c').grid(row=1, column=1)
# Button(text = '2', bg="#cff210", height = 2, width = 6, fg='#172c6c').grid(row=1, column=2)
# Button(text = '3', bg="#651ca7", height = 2, width = 6, fg='#f11daf').grid(row=2, column=0)
# Button(text = '3', bg="#651ca7", height = 2, width = 6, fg='#f11daf').grid(row=2, column=1)
# Button(text = '3', bg="#651ca7", height = 2, width = 6, fg='#f11daf').grid(row=2, column=2)
# Button(text = '4', bg="#973d66", height = 2, width = 6, fg='#b9f754').grid(row=3, column=0)
# Button(text = '4', bg="#973d66", height = 2, width = 6, fg='#b9f754').grid(row=3, column=1)
# Button(text = '4', bg="#973d66", height = 2, width = 6, fg='#b9f754').grid(row=3, column=2)


# Label(text="Имя:").grid(row=0, column=0)
# table_name = Entry(width=30)
# table_name.grid(row=0, column=1, columnspan=3)
 
# Label(text="Столбцов:").grid(row=1, column=0)
# table_column = Spinbox(width=7, from_=1, to=50)
# table_column.grid(row=1, column=1)
# Label(text="Строк:").grid(row=1, column=2)
# table_row = Spinbox(width=7, from_=1, to=100)
# table_row.grid(row=1, column=3)
 
# Button(text="Справка").grid(row=2, column=0)
# Button(text="Вставить").grid(row=2, column=2)
# Button(text="Отменить").grid(row=2, column=3)

#place():
# L1 = ttk.Label(root, text = "Physics")
# L1.place(x = 10,y = 10)
# E1 = ttk.Entry(root)
# E1.place(x = 60,y = 10)
# L2 = ttk.Label(root,text = "Maths")
# L2.place(x = 10,y = 50)
# E2 = ttk.Entry(root)
# E2.place(x = 60,y = 50)

# L3 = ttk.Label(root,text = "Total")
# L3.place(x = 10,y = 150)
# E3 = ttk.Entry(root)
# E3.place(x = 60,y = 150)

# B = Button(root, text = "Add")
# B.place(x = 100, y = 100)

root.mainloop()