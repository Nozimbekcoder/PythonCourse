"""
Muallif: Nozimjon Bozorov
Sana: 29.03.2022
Mavzu: Fayllar bilan ishlash
"""

# import platform
# x = platform.system()
# print(x)

# file = open('sinov.txt', 'w')
# file.write('Bu bizning 1-qo\'shilgan matnimiz')
# file.close()
# print('Yangi fayl muvaffaqiyatli yaratildi!')
#
# file = open('sinov2.txt', 'w')
# file.write('Bu bizning yangi matnimiz')
# file.close()
# print('Yangi fayl muvaffaqiyatli yaratildi!')
#
# file = open('sinov.py', 'w')
# file.write("print('salom hammaga')")
# file.close()
# print('Yangi fayl muvaffaqiyatli yaratildi!')


# f = open('sinov.txt','r')
# print(f.read())
# f.close()

"""
Fayllar bilan ishlash pythonda muhim qismlardan biri. Ayniqsa, web dasturlar bilan 
ishlashda. Pythonda fayllarni hosil qilish, o’qish, yangilash va o’chirish imkoniyati mavjud.
Fayllarni ochish open() funksiyasi bilan amalga oshadi. Bunda ushbu funksiya 2 ta parameter 
qabul qiladi: Fayl nomi va rejimi. Rejim deganda faylni qay maqsadda ochish nazarda 
tutiladi. Bu rejimlar quyidagilar:
 “r” – Read – faylni o’qish uchun ochish. Agar fayl mavjud bo’lmasa, xatolik yuz beradi.
 “a” – Append – faylga qo’shimcha qo’shish uchun ochish. Agar fayl mavjud bo’lmasa 
yangi fayl ochadi. 
 “w” – Write – faylga yozish uchun ochish. Agar fayl mavjud bo’lmasa, yangi fayl 
ochadi.
 “x” – Create – yangi fayl hosil qilish. Agar bunday fayl mavjud bo’lsa xatolik yuz 
beradi.
"""

# f= open('salom.txt','x')
# f.close()

# a   append yordamida fayllarga malumotlar qoshish

# file = open('ap.txt', 'a')
# file.write('Ramazon Muborak')
# file.write('\n')
# file.close()
#
# f=open('ap.txt','a')
# f.write('2-aprel')
# f.write('\n')
# f.close()


# b = open('D:\Sistema OS\eest.txt','a')
# b.write('sistema diskida joylashgan eest.txt fayli')
#
# b.close()


# b = open('ap.txt', 'r')
# print(b.read(60))
#
# b.close()


b = open('ap.txt', 'r')
print(b.readline())
print(b.readline())
print(b.readline())
print(b.readline())
print(b.readline())

b.close()