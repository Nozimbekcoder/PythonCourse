from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

import googletrans
from googletrans import Translator

root = Tk()
root.title('GoogleTarjimon_v3.0')

window_width = 1080
window_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# root.configure(background='white')


def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1.title())
    label2.configure(text=c2.title())
    root.after(500, label_change)


def translate_now():
    try:
        text = text1.get(1.0,END)
        t1 = Translator()
        trans_text = t1.translate(text,src=combo1.get(),des=combo2.get())
        trans_text=trans_text.text

        text2.delete(1.0, END)
        text2.insert(END,trans_text)
    except:
        pass
        # if text1.get() == '':
        #     showerror(title='Hisobot', message='Tarjima qilish uchun matn kiritilmadi!')
        # else:
        #     showerror(title='Hisobot', message='Iltimos Internetga Ulanishingizni\n'
        #                                        'Tekshirib Ko\'ring!')


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

# 111111111111111111111111111111111111111111111111111111111

combo1 = ttk.Combobox(root, values=languageV, font='Roboto 14', state='r',cursor='hand2')
combo1.place(x=110, y=20)
combo1.set('ENGLISH')

label1 = Label(root, text='ENGLISH', font="segoe 30 bold", bg='white', width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# 22222222222222222222222222222222222222222222222222222222222222222222222

combo2 = ttk.Combobox(root, values=languageV, font='Roboto 14', state='r',cursor='hand2')
combo2.place(x=730, y=20)
combo2.set('TILNI TANLANG')

label2 = Label(root, text='UZBEK', font="SEGOE 30 bold", bg='white', width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# 1-text

f1 = Frame(root, bg='black', bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font='Roboto 20', bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side='right', fill=Y)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



# 2-text

f2 = Frame(root, bg='black', bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font='Roboto 20', bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side='right', fill=Y)

scrollbar1.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

tarjima = Button(root,text='Tarjima',font="Roboto 15", activebackground='white',
                 cursor='hand2',bd=1,width=10,height=2,bg='black',fg='white',
                 command=translate_now)
tarjima.place(x=476,y=250)






label_change()
root.mainloop()
