"""
12/05/2022
Lesson 11

Mavzu: Pythoning standart Tkinter kutubxonasi   LabelFrame, Frame,
"""

from tkinter import *
from tkinter.messagebox import *

import wikipedia
wikipedia.set_lang('uz')

root = Tk()
root.title("WikipediaUz")
root.geometry("700x400")
root.resizable(False, False)
root.configure(background='#709900')


def dhaqida():
    lframe = LabelFrame(root, text="Dastur haqida", bg='#709900')
    lframe.pack(fill=BOTH, expand=True)
    haqida = Label(lframe, text="Haqida\n"
                                "Biz bu dasturni Python kursi\n"
                                "davomida 9-10-11 darslarda\n"
                                "tuzganmiz", bg='#709900').pack()


menubar = Menu(root, bg='black', fg='white')
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Asosiy", menu=filemenu)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="Dastur Haqida", command=dhaqida)
aboutmenu.add_separator()
aboutmenu.add_command(label="Muallif Haqida")
menubar.add_cascade(label="Haqida", menu=aboutmenu)


def qu():
    root.quit()


chiqish = Menu(menubar, tearoff=0)
chiqish.add_command(label="Chiqish", command=root.destroy)
menubar.add_cascade(label="Chiqish", menu=chiqish)

root.configure(menu=menubar)
sarlavha_l = Label(root, text="WikipediaUz", font="Arial 20", justify=CENTER, width=37, bg='#bbff00').pack()
qidiruv_l = Label(root, text="Qidiruv:", fg='white', font="Arial 15", justify=LEFT, width=15, bg='#709900').place(x=50,
                                                                                                                  y=50)
search_e = Entry(root, font="Arial 15", justify=LEFT, width=30)
search_e.place(x=190, y=50)
lb= Listbox(root, font="Arial 15", width=16, height=10, bg='#bbff00')




lb.place(x=5, y=90)
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "PHP")
lb.insert(5, "JavaScript")
lb.insert(6, "HTML")

#--------------------------------------------------------------


scrollbar = Scrollbar(root)
scrollbar.place(anchor=NE, x=700, y=90, height=302)

matn_t = Text(root, font="Arial 15", width=44, height=13, wrap=WORD, yscrollcommand=scrollbar.set)
scrollbar.config(command=matn_t.yview)
matn_t.place(x=190, y=90)



#--------------------------------------------------------

def qidiruv_funk():
    s = search_e.get()
    try:
        r = wikipedia.summary(s)
        matn_t.insert(1.0, str(r))
    except:
        showerror(title="Xatolik", message="Xatolik yuz berdi")
        print("Xatolik yuz berdi")


# qimage = PhotoImage(file="search_ico.png")
# qidir = Button(root, image=qimage,width=100, font="Arial 12", command=qidiruv_funk).place(x=540, y=48)

def tozala():
    matn_t.delete(1.0, END)


qidir_b = Button(root, text='Qidir', font="Arial 12", command=qidiruv_funk).place(x=540, y=48)
tozala_b = Button(root, text='Tozala', font="Arial 12", command=tozala).place(x=595, y=48)

root.mainloop()
