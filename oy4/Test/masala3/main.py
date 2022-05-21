from tkinter import *
from tkinter.messagebox import *
from datetime import date

hozirgiyil = date.today().year
root = Tk()
root.title("Oy4")
window_width = 800
window_height = 400
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(width=False, height=False)

root.configure(bg='#00001a')
Label(root, text='User Registrator', font=('Sans serif', 32, 'bold'), justify=CENTER).pack()

ism = Label(root, text="Ism:", font=("Arial", 17), bg='#00001a', fg='white').place(x=10, y=90)
ism_e = Entry(root, font=("Arial", 17), width=17)
ism_e.place(x=150, y=90)

familiya = Label(root, text="Familiya:", font=("Arial", 17), bg='#00001a', fg='white').place(x=420, y=90)
familiya_e = Entry(root, font=("Arial", 17), width=17)
familiya_e.place(x=540, y=90)

tyil = Label(root, text="Tugilgan yil:", font=("Arial", 17), bg='#00001a', fg='white').place(x=10, y=150)
tyil_e = Entry(root, font=("Arial", 17), width=17)
tyil_e.place(x=150, y=150)

manzil = Label(root, text="Manzil:", font=("Arial", 17), bg='#00001a', fg='white').place(x=420, y=150)
manzil_e = Entry(root, font=("Arial", 17), width=17)
manzil_e.place(x=540, y=150)

fayln = Label(root, text="Fayl nomi:", font=("Arial", 17), bg='#00001a', fg='white').place(x=10, y=210)
fayln_e = Entry(root, font=('Arial',17),width=18)
fayln_e.place(x=150,y=210)
#

def saqla():
        try:
            # file_name = asksaveasfilename(initialdir='D:\Programmer\GitHub\PythonCourse\oy4\Test\Javoblar',defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
            file_name = fayln_e.get()
            with open(f'D:\Programmer\GitHub\PythonCourse\oy4\Test\Javoblar\{file_name}.txt', 'a') as text_file:
                text_file.write(f"\n"
                                f"-----------------------------------------------------------\n"
                                f"ISM:          {ism_e.get()}\n"
                                f"FAMILYIA:     {familiya_e.get()}\n"
                                f"YOSHI:        {hozirgiyil-(int(tyil_e.get()))}\n"
                                f"TUGILGAN YIl: {tyil_e.get()}\n"
                                f"MANZILI:      {manzil_e.get()}\n"
                                f"-----------------------------------------------------------")
            showinfo(title="Hisobot", message="Ma'lumotlar muvaffaqilyatli saqlandi!")
            holat = Label(root, text="Ma'lumotlar muvaffaqilyatli saqlandi!", font=('Arial 30 bold '), fg='green')
            holat.place(x=50, y=280)

            def labdel():
                holat.destroy()

            holat.after(1500,labdel)


        except:
            showerror(title="Hisobot", message="Ma'lumotlarni saqlashda xatolik")
            def dele():
                fayln_e.delete(0,END)

            ism_e.delete(0,END)
            familiya_e.delete(0,END)
            tyil_e.delete(0,END)
            manzil_e.delete(0,END)
            fayln_e.after(500,dele)




ok_b = Button(root, text="Saqlash", font=("Times New Roman", 17), justify=CENTER, padx=123,command=saqla).place(x=433, y=200)

root.mainloop()
