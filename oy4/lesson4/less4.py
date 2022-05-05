"""
lesson4
Muallif: Nozimjon Bozorov
Sana: 23.04.2022
Mavzu: Pythoning standart Tkinter kutubxonasi vidgetlarni yaratish
"""

"""
Tugmalar

activeforeground - aktiv tugma rangi
activebackground - Aktiv tugma fon rangi
foreground | fg - tugma rangi
background | bg - tugma fon rangi
font=('Arial 18') - tugmaning fonti Shrift turi olchami (family, size, weight)
command - tugma bosilganda chaqiriladigan funksiya, yoki funksiyalar ro'yxati
height('') - tugmaning balandligi
width('') - tugmaning kengligi
bd - tugma chegarasi qalinligi
padx=15 - tugmaning ikki tomonidan qoshimcha kenglik berish
pady=15 - tugmaning tepasidan va pastidan qoshimcha kenglik berish
justify('center') - tugmaning matn o'rnatish turi (center, left, right)
state('disabled') - tugmaning holatini belgilash (normal, disabled, readonly, active)
relief - chegara turini belgilash (flat, groove, raised, ridge, solid, sunken)
underline - matnning tagiga chizish unda qo'yishni belgilash (0, 1)
wraplength - matnning qo'yishni belgilash (0, 1)


"""

"""
Joylashtirish usullar: pack(), grid(), place()

1.pack() - joylashtirish usuli
2.grid(row=0,column=0) - joylashtirish usuli
3.place(x=0,y=0) - joylashtirish usuli

1.pack() - joylashtirish usuli

widget.pack(pack_options)
expand - bosh joyni toldirish
fill - joyni to'ldirish turi (both, x, y)
side - joyni to'ldirish joyini belgilash (top, bottom, left, right)
----------------------------------------------------------------------
2.grid(row=0,column=0) - joylashtirish usuli

column=n (ustun) - Vidjetni joylashtiradigan ustun; standart 0 (eng chap ustun).
row=n (qator) - Vidjetni joylashtiradigan qator; standart 0 (eng chap ustun).
columnspan - ustun qancha  vidjetni egallaydi; standart 1
rowspan - qator qancha  vidjetni egallaydi; standart 1

"""

from tkinter import *

root = Tk()
root.title("Tugmalar")
root.geometry('700x400')

# tugma = Button(root, text='1-Tugma', font=('Arial 28'),
#            activebackground='yellow', activeforeground='red', fg='yellow',
#            bg='red', bd=8, padx=50, relief='raised',
#            underline=-1, wraplength=0).pack(fill=BOTH, expand=1)

t1 = Button(root, text='row: 0 ; column: 0', font=('Arial 28'), ).grid(row=0, column=0)
t2 = Button(root, text='row: 0 ; column: 1', font=('Arial 28'), ).grid(row=0, column=1)
t3 = Button(root, text='row: 0 ; column: 2', font=('Arial 28'), ).grid(row=0, column=2)
t4 = Button(root, text='row: 1 ; column: 0', font=('Arial 28'), ).grid(row=1, column=0)
t5 = Button(root, text='row: 1 ; column: 1', font=('Arial 28'), ).grid(row=1, column=1)
t6 = Button(root, text='row: 1 ; column: 2', font=('Arial 28'), ).grid(row=1, column=2)
t7 = Button(root, text='row: 2 ; column: 0', font=('Arial 28'), ).grid(row=2, column=0)
t8 = Button(root, text='row: 2 ; column: 1', font=('Arial 28'), ).grid(row=2, column=1)
t9 = Button(root, text='row: 2 ; column: 2', font=('Arial 28'), ).grid(row=2, column=2)

root.mainloop()
