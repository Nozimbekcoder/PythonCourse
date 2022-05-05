"""
lesson5
Muallif: Nozimjon Bozorov
Sana: 26.04.2022
Mavzu: Pythoning standart Tkinter kutubxonasi grid
"""

"""
Tkinter grid () metodi

Mana mumkin bo'lgan parametrlar ro'yxati :
 column (ustun) - Vidjetni joylashtiradigan ustun; standart 0 (eng chap ustun).
 columnspan - qancha ustun vidjetni egallaydi; standart 1.
 ipadx, ipady - Vidjet chegaralarida gorizontal va vertikal ravishda vidjetni to'ldirish uchun 
qancha piksel.
 padx, pady - v chegaralaridan tashqarida gorizontal va vertikal ravishda vidjetni qancha 
pikselga to'ldirish kerak.
 row (qator) - vidjetni joylashtiradigan qator; sukut bo'yicha hali ham bo'sh bo'lgan birinchi 
qator.
 rowspan - nechta qatorli vidjet egallaydi; standart 1.
 stick (yopishqoq) - Agar katak vidjetdan kattaroq bo'lsa, nima qilish kerak. Odatiy bo'lib, 
sticky = " bilan vidjet o'z katakchasida joylashgan. yopishqoq bo'lishi mumkin, nol yoki 
undan ko'p N, E, S, W, NE, NW, SE va SW ning biriktirilishi, vidjet yopishgan katakning 
yon va burchaklarini ko'rsatadigan kompas yo'nalishlari


"""

# from tkinter import *
#
# oyna = Tk()
# oyna.title("Label vs Entry")
# oyna.geometry("400x500")
# oyna.configure(bg="lightblue")
# oyna.resizable(False, False)
#
# ismlar = Label(oyna, text="Ism:", bg="lightblue", fg="red", font=("Times", 18, "bold"))
# ismlar.grid(row=0, column=0)
#
# ismkiritish = Entry(oyna,bd=10, font=("Times", 18, "bold")).grid(row=0, column=1)
#
# ismlar1 = Label(oyna, text="Famliya:", bg="lightblue", fg="red", font=("Times", 18, "bold"))
# ismlar1.grid(row=1, column=0)
#
# ismkiritish1 = Entry(oyna, font=("Times", 18, "bold")).grid(row=1, column=1)
#
# label = Label(oyna, text="Passwod:", fg="red", font=("Times", 18, "bold")).grid(row=2, column=0)
# entry = Entry(oyna, show="*", font=("Times", 18, "bold")).grid(row=2, column=1)
#
#
# oyna.mainloop()



from tkinter import *
oyna = Tk()
oyna.title("Calculator")
oyna.geometry("414x500")
oyna.configure(bg="#00001a")
oyna.resizable(False, False)

ekran = Entry(oyna, bd=5 , font=("Arial 27"),width=19)
ekran.grid(row=0, column=0, columnspan=4, pady=5,padx=10)

ce = Button(oyna, text="CE", font=("Arial", 20), bg="white", fg="black")
ce.grid(row=1, column=0, padx=10)
c = Button(oyna, text="C", font=("Arial", 20), bg="white", fg="black")
c.grid(row=1, column=1, padx=10)

tozala = Button(oyna, text="<×", font=("Arial", 20), bg="white", fg="black")
tozala.grid(row=1, column=2, padx=10)

bolinma = Button(oyna, text="/", font=("Arial", 20), bg="white", fg="black")
bolinma.grid(row=1, column=3, padx=10)

yetti = Button(oyna, text="7", font=('Arial',20), bg='white', fg='black')
yetti.grid(row=2, column=0, padx=10,pady=10)

sakkiz = Button(oyna, text="8", font=('Arial',20), bg='white', fg='black')
sakkiz.grid(row=2, column=1, padx=10,pady=10)

toqqiz = Button(oyna, text="9", font=('Arial',20), bg='white', fg='black')
toqqiz.grid(row=2, column=2, padx=10,pady=10)

kopaytir = Button(oyna, text="*", font=('Arial',20), bg='white', fg='black')
kopaytir.grid(row=2, column=3, padx=10,pady=10)

tort = Button(oyna, text="4", font=('Arial',20), bg='white', fg='black')
tort.grid(row=3, column=0, padx=10,pady=10)

besh = Button(oyna, text="5", font=('Arial',20), bg='white', fg='black')
besh.grid(row=3, column=1, padx=10,pady=10)

olti = Button(oyna, text="6", font=('Arial',20), bg='white', fg='black')
olti.grid(row=3, column=2, padx=10,pady=10)

minus = Button(oyna, text="-", font=('Arial',20), bg='white', fg='black')
minus.grid(row=3, column=3, padx=10,pady=10)

bir = Button(oyna, text="1", font=('Arial',20), bg='white', fg='black')
bir.grid(row=4, column=0, padx=10,pady=10)

ikki = Button(oyna, text="2", font=('Arial',20), bg='white', fg='black')
ikki.grid(row=4, column=1, padx=10,pady=10)

uch = Button(oyna, text="3", font=('Arial',20), bg='white', fg='black')
uch.grid(row=4, column=2, padx=10,pady=10)

plus = Button(oyna, text="+", font=('Arial',20), bg='white', fg='black')
plus.grid(row=4, column=3, padx=10,pady=10)

plmin = Button(oyna, text="±", font=('Arial',20), bg='white', fg='black')
plmin.grid(row=5, column=0, padx=10,pady=10)

nol = Button(oyna, text="0", font=('Arial',20), bg='white', fg='black')
nol.grid(row=5, column=1, padx=10,pady=10)

nuqta = Button(oyna, text=".", font=('Arial',20), bg='white', fg='black')
nuqta.grid(row=5, column=2, padx=10,pady=10)

teng = Button(oyna, text="=", font=('Arial',20), bg='white', fg='black')
teng.grid(row=5, column=3, padx=10,pady=10)

oyna.mainloop()

