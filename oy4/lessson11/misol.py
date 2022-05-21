# from tkinter import *
#
# root = Tk()
# root.geometry("500x500")
#
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# mylist = Listbox(root, yscrollcommand=scrollbar.set)
#
# for line in range(1000):
#     mylist.insert(END, "This is line number " + str(line))
#     mylist.pack(side=LEFT, fill=BOTH)
#     scrollbar.config(command=mylist.yview)
#
# root.mainloop()
#
#
# from tkinter import *
# from tkinter.messagebox import *
# top = Tk()
# Lb1 = Listbox(top, font="italic")
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Java")
# Lb1.insert(3, "C++")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JavaScript")
# Lb1.insert(6, "HTML")
# Lb1.pack()
# top.mainloop()
#
# import wikipedia
#
# wikipedia.set_lang('uz')
#
# print(wikipedia.search(input("")))


from tkinter import *
from tkinter.ttk import *
from turtle import width

root = Tk()
for i in range(10):
    print(i)

combo1= Combobox(root, values=("Python", "Java", "C++", "PHP", "JavaScript", "HTML"),font="arial 12",width=18)
combo1.set("Java")
combo1.pack()


root.mainloop()