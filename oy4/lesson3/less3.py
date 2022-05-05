"""
lesson3
Muallif: Nozimjon Bozorov
Sana: 21.04.2022
Mavzu:  Pythoning tashqi kutubxonasi, Pythoning standart Tkinter kutubxonasi
"""

# from googletrans import Translator
#
# tarjimon = Translator()
#
# matn = 'hello world'
#
# tarjima = tarjimon.translate(matn, dest='ru')
#
# print(tarjima)


"""
Tkinter dasturlash  'Grafik foydalanuvchi interfeysi'
Tkinter - Python uchun standart GUI kutubxonasi.
Python Tkinter bilan birgalikda GUI dasturlarini yaratishning
tez va oson usulini taqdim etadi.
Tkinter Tk GUI asboblar
to'plamiga kuchli ob'ektga yo'naltirilgan interfeysni 
taqdim etadi. Tkinter yordamida GUI
dasturini yaratish oson ish.
Sizga kerak bo'lgan narsa - bu quyidagi amallarni bajarishdir:
 Tkinter modulini import qilish.
GUI dasturining asosiy oynasini yaratish. GUI dasturiga
bir yoki bir nechta vidjet qo'shish. Foydalanuvchi tomonidan
qo'zg'atilgan har bir hodisaga qarshi choralar ko'rish uchun asosiy
voqea tsiklini kiritish.
Pythonda Tkinter modulini 2 usulda import qilish mumkin !!!
1 - usul

import tkinter
top = tkinter.Tk()
# Vidjetlarni qo'shish uchun kod bu yerga yoziladi ... 
top.mainloop()

2 - usul
from tkinter import *
top = Tk()
# Vidjetlarni qo'shish uchun kod bu yerga yoziladi ... 
top.mainloop()
Bu ikkila yozgan kodimiz quyidagi oynani yaratadi:
"""

# import tkinter
# top = tkinter.Tk()
# # Vidjetlarni qo'shish uchun kod bu yerga yoziladi ...
# top.mainloop()
# Button vidjeti sizning ilovangizdagi tugmalarni ko'rsatish uchun ishlatiladi.

from tkinter import *

root = Tk()
root.geometry("600x350")
root.title("1-dasturimiz")
root.configure(background="gold")


def ok1():
    a=Label(root, text="Salom", font=('Arial 28'))
    a.pack()


ok = Button(root, text='Yozmoq', font=('Georgia 16'), background='green', foreground='white',
            activeforeground='green', activebackground='white',height=2,width=15, command=ok1)
ok.pack()

root.mainloop()
