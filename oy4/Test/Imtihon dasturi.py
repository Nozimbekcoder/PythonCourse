from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *

oyna = Tk()
# dastur sarlavhasi "Python registrator"ga o'zgartirldi
oyna.title("Python registrator")
oyna.geometry("570x600")  # oyna o'lchami belgilandi
oyna.config(bg="green", bd=10)  # oyna foniga yashil rang berildi

labal_salom = Label(master=oyna, font=100, fg="red", bg="white",
                    text="Salom Python Kurslarimizga yozilmoqchimisiz?")
# labelda oyna aks etdi : Python kurslarimizga yozilmoqchimisiz?
labal_salom.place(x=55, y=20)  # label joylashtirildi

# ismingiz nomli label oynaga qoshildi
username_labal = Label(oyna, text="Ismingiz:", font=50)
username_labal.place(x=20, y=65)  # Ismingiz # label joylashtirildi

kirituchi_joy1 = Entry(oyna, font=100, bd=2, fg="RED", width=27)
kirituchi_joy1.place(x=180, y=65)  # label joylashtirildi

username_labal2 = Label(oyna, text="Familyangiz:", font=50)
username_labal2.place(x=20, y=130)  # label joylashtirildi

kirituchi_joy2 = Entry(oyna, font=100, bd=2, fg="RED", width=27)
kirituchi_joy2.place(x=180, y=130)  # label joylashtirildi

username_labal3 = Label(oyna, font=100, text="Tel raqamingiz:")
username_labal3.place(x=20, y=195)  # label joylashtirildi

kirituchi_joy3 = Entry(oyna, font=100, bd=2, fg="RED", width=27)
kirituchi_joy3.place(x=180, y=195)

username_labal4 = Label(oyna, font=100, text="Elektron pochta:")
username_labal4.place(x=20, y=260)  # label joylashtirildi

kirituchi_joy4 = Entry(oyna, font=100, bd=2, fg="RED", width=27)
kirituchi_joy4.place(x=180, y=260)  # entry  elektron pochta joylashtirlidi


# CheckVar1 = IntVar()
# c1 = Checkbutton(oyna, text="Kiritilgan ma'lumotlarim to'griligiga ishonch hosil qildim",
# variable=CheckVar1, onvalue=1,offvalue=0,width=50, font=50, selectcolor="orange")

# c1.place(x=10, y=300)


def ariza_tugmasi():
    # global ism, familya, telefon_raqami, elektron_pochtasi, a1, f
    global royh
    ism = kirituchi_joy1.get()

    familya = kirituchi_joy2.get()

    telefon_raqami = kirituchi_joy3.get()
    telefon_raqami2 = type(telefon_raqami)
    tele2 = str(telefon_raqami)
    telefon_raqami1 = len(tele2)
    tel = 13

    elektron_pochtasi = kirituchi_joy4.get()

    if ism == "":
        showwarning(
            message="Iltimos Ismingizni kiriting!\nSiz ismingizni kiritmadingiz☝")

    elif familya == "":
        showwarning(
            message="Iltimos Familyangizni kiriting!\nSiz Familyangizni kiritmadingiz☝")

    elif telefon_raqami == "" and telefon_raqami1 < tel and telefon_raqami2 == int:

        showwarning(
            message="Iltimos Telefon rqamingizni kiriting!\n"
                    "Siz Telefon raqamingizni noto'gri kiritdingiz☝\n"
                    "Namuna: +998XX XXX XX XX")

    elif telefon_raqami1 < 13 and not telefon_raqami1 > 14:
        showwarning(
            message="Iltimos Telefon rqamingizni kiriting!\n."
                    "Siz Telefon raqamingizni noto'gri kiritdingiz☝\n"
                    "Namuna: +998XX XXX XX XX")

    elif elektron_pochtasi == "":
        showwarning(
            message="Iltimos elektron pochtangizni kiriting!\nSiz elektron pochtangizni kiritmadingiz")

        # showwarning(message="Arizangiz qabul qilindi Sizga tez orada xabar qilamiz!")
    else:

        askquestion(title="Kiritilgan ma'lumotlar",
                    message=f"O\'quvchining ismi:      {ism}\n"
                            f"O\'quvchining Familyasi: {familya}"
                            f"\nTelefon raqami:        {tele2}\n"
                            f"Elektron pochtasi:       {elektron_pochtasi}\n")

        # showwarning(message="Itimos to'ldirilishi kerak bo'lgan joylarni to'ldiring!")
        showwarning(
            message="Sizni ma'lutlaringiz Muvaffaqiyatli saqlandi,\n"
                    "Sizga Tez orada quyidagi raqamdan telefon qilamiz\n"
                    "              +998930576603\n"
                    "Yoki elektron manzilingizga xabar yuboramiz")
        kirituchi_joy1.delete(0, END)

        kirituchi_joy2.delete(0, END)

        kirituchi_joy3.delete(0, END)

        kirituchi_joy4.delete(0, END)

    with open("Python_oquvchilar_royhati.txt", "a") as f:
        f.write(
        f"O\'quvchining ismi:      {ism}\n"
        f"O\'quvchining Familyasi: {familya}\n"
        f"Telefon raqami:          {tele2}\n"
        f"Elektron pochtasi:       {elektron_pochtasi}\n"
        f"\n")
        
        royh=f.read()
    # f.close()


arizani_yuborish_tugmasi = Button(oyna, font=100, fg="yellow", bg="red", activeforeground="red",
                                  activebackground="yellow",
                                  text="Arizani yuborish", command=ariza_tugmasi)

arizani_yuborish_tugmasi.place(x=290, y=340)

chiqish_tugmasi = Button(oyna, font=100, text="Chiqish", fg="yellow", bg="green", activeforeground="green",
                         activebackground="yellow", command=oyna.quit)
chiqish_tugmasi.place(x=470, y=540)


def dastur_haqida_funk():
    laframe = LabelFrame(oyna, text="Dastur haqida", font=100)
    laframe.pack(fill="both", expand="yes")
    labl = Label(laframe, font=100, text="Bu dastur yordamida siz o'quvchilarni\n"
                                         "guruhga to'plash uchun foydalansa bo'ladi.\n"
                                         "Dastur to'liq bepul tarzda Bozorov Nozimjon\n"
                                         "tomonidan  beriladi.\n"
                                         "Dasturdan foydalanish juda oson\n"
                                         "Berilgan punktlar to'ldiriladi va\n"
                                         "arizani yuborish tugmasi bosiladi\n"
                                         "Agarda biror-bir ma'lumtot kirilmasa dastur bu haqida\n"
                                         "Ogohlantiradi va qayta to'ldirsh kerak bo'ladi,\n"
                                         "yoki mavjud xatolar tuzatiladi qaytadan urinib ko'riladi.\n"
                                         "Agar kiritilgan ma'lumotlar tog'ri to'ldirilsa\n"
                                         "ma'lumotlar qabul qilinadi va ko'rsatilgan raqamdan\n"
                                         "qo'ng'iroq qilinishi kutiladi")

    labl.pack(fill="both", expand="yes")
    labl


dastur_haqida = Button(oyna, width=3, font=100, text="D\na\ns\nt\nu\nr\n\nh\na\nq\ni\nd\na", fg="white",
                       bg="black", activebackground="white", activeforeground="black", command=dastur_haqida_funk)
dastur_haqida.place(x=509, y=20)


def muallif():
    labelframe = LabelFrame(oyna, bg="teal", font=100,
                            text="Bu dastur muallifi haqida")
    labelframe.pack(fill="both", expand="yes")
    left = Label(labelframe, bg="blue", font=100, text="Bu ilova 12-iyun 2021-yil \n"
                                                       "Dasturchi Nozimjon Bozorov \n"
                                                       "Ishlab chiqarilgan\n"
                                                       "Ishlab chiqaruvchi Bozorov Nozimjon\n"
                                                       "V0.0.1")

    left.place(x=100, y=10)
    right = Label(labelframe, bg="blue", fg="black", font=80,
                  text="Barcha xizmatlar dasturchi tomonidan himoyalangan\nva nazorat qilinadi!")
    right.place(x=40, y=430)
    boglanish_uchun = Label(labelframe, bg="grey", fg="yellow",
                            font=50, text="Elektrpn pochta:  Nozimbek6603@gmail.com\n")

    boglanish_uchun.place(x=140, y=490)

    boglanish_uchun1 = Label(labelframe, bg="grey", fg="yellow",
                             font=50, text="Telefon raqami:   +998 93 057 66 03")
    boglanish_uchun1.place(x=140, y=514)


muallif_tugmasi = Button(oyna, font=100, text="Muallif haqida", fg="yellow",
                         bg="teal", activeforeground="teal", activebackground="yellow", command=muallif)
muallif_tugmasi.place(x=2, y=540)


def admin():
    oyna1 = Tk()
    oyna1.title("Administrator")
    oyna1.geometry("450x300")
    oyna1.config(bg="blue")
    username = Label(oyna1, font=100, width=30, text="Parolni kiriting")
    username.place(x=57, y=20)

    kr_parol = Entry(oyna1, font=100, width=34, bd=2, show="*")
    kr_parol.place(x=35, y=60)

    def admin_oynasi():

        tparol1 = kr_parol.get()
        tparol = str(tparol1)
        if tparol == "0000":
            boshqaruv_oynasi = Tk()
            boshqaruv_oynasi.title("Administrator")
            boshqaruv_oynasi.geometry("400x500")
            boshqaruv_oynasi.config(bg="pink")
            nframe = LabelFrame(boshqaruv_oynasi, font=100,
                                text="O'quvchilar ro'yhati")
            nframe.pack(fill="both", expand="yes")
            royhat= Label(nframe, text=royh)
            royhat.pack()

            def py_royhat():
                
                
                
                pass

            # f = open("Python_oquvchilar_royhati.txt", "r")
            # # nishon = Label(admin_oynasi, font=100, text=f)

            # f.close()

            yangilash = Button(nframe, text="Yangilash", command=py_royhat)
            yangilash.place(x=300, y=445)

            boshqaruv_oynasi.mainloop()
        else:
            showerror(message="Kirtilgan parol\n    Notog'ri")

    parol_tugmasi = Button(oyna1, width=10, font=100, fg="green", bg="white",
                           activebackground="yellow", activeforeground="red", text="✔\nOK", command=admin_oynasi)
    parol_tugmasi.place(x=295, y=100)

    def toliq():
        showinfo(message="Bu funksiya hali to'liq ishlab chiqilmagan")

    parolni_unutdingizmi = Button(oyna1, width=34, font=15, text="Parolni unutdingizmi?",
                                  fg="red", bg="white", activebackground="red", activeforeground="white", command=toliq)

    parolni_unutdingizmi.place(x=35, y=170)

    oyna1.mainloop()


administrator_tugmasi = Button(oyna, font=100, width=20, text="Administror", fg="yellow",
                               bg="blue", activeforeground="blue", activebackground="yellow", command=admin)
administrator_tugmasi.place(x=150, y=540)


def baholash():
    oyna_baholash = Tk()
    oyna_baholash.title("Baholash")
    oyna_baholash.config(bg="green")
    

    def baho():
        showinfo(message="Dasturni baholaganinggiz uchun rahmat!😊")

    yaxshi_tugmasi = Button(oyna_baholash, font=100, width=10, bg="yellow", fg="red",
                            activebackground="red", activeforeground="yellow", text="😊\nYaxshi", command=baho)
    yaxshi_tugmasi.grid(row=0, column=0)

    zor_tugmasi = Button(oyna_baholash, font=100, width=10, bg="yellow", fg="red",
                         activebackground="red", activeforeground="yellow", text="😁\nNormal", command=baho)
    zor_tugmasi.grid(row=0, column=1)

    udar_tugmasi = Button(oyna_baholash, font=100, width=10, bg="yellow", fg="red",
                          activebackground="red", activeforeground="yellow", text="🤣\nZo'r", command=baho)
    udar_tugmasi.grid(row=0, column=2)

    oyna_baholash.mainloop()


dasturni_baholash = Button(oyna, width=5, font=100, text="😍", fg="green", bg="yellow",
                           activeforeground="yellow", activebackground="green", command=baholash)
dasturni_baholash.place(x=394, y=540)

# lable=Label(oyna,font=100,text="24/7",width=10)
# lable.place(x=250,y=420)

oyna.mainloop()

# # import re
# # andoza="[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
