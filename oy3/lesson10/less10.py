"""
lesson9
Muallif: Nozimjon Bozorov
Sana: 09.04.2022
Mavzu: RegEx, Json va pip
"""
# from time import strftime
# from tkinter import *
# from tkinter.ttk import*
# root = Tk()
# root.title('Soat')
# def time():
#     soat = strftime('%H:%M:%S\n%A\n%Y/%B')
#     label.config(text=soat)
#     label.after(1000,time)
#
#
# label = Label(root, font=('ds-digtal',80), foreground='cyan', background='black')
# label.pack(anchor='center')
# time()
# mainloop()


# """Python RegEx"""
#
# '''
# RegEx yoki Regular Expression - qidiruv sxemasini tashkil etuvchi belgilar ketma-ketligi.
#
# RegEx-dan satrda belgilangan qidiruv namunasi mavjudligini tekshirish uchun foydalanish mumkin.
#
# RegEx yoki Regular Expression - qidiruv sxemasini tashkil etuvchi belgilar ketma-ketligi.
#
# RegEx-dan satrda belgilangan qidiruv namunasi mavjudligini tekshirish uchun foydalanish mumkin.
# '''
#
# import re
# import os
# shablon = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
#
# belgi = 1
# while belgi:
#     email = input('Emailingizni kiriting:')
#     if email!='q':
#         if re.match(shablon, email):
#             print('email tog\'ri', email)
#             with open('email.txt', 'a') as f:
#                 f.write(f'{email}\n\n')
#             print('Siz kiritgan email saqlab qolindi.')
#             continue
#         else:
#             print('email notog\'ri', email)
#             if os.path.exists('email.txt'):
#                 os.remove('email.txt')
#                 print('Email.txt fayli ochirib yuborildi')
#             print('Siz kiritigan email saqlab qolinmadi')
#     else:
#         belgi = 0
#         print('Dastur yakunlandi')
