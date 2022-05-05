"""
lesson8
Muallif: Nozimjon Bozorov
Sana: 5.04.2022
Mavzu: Fayllar bilan ishlash
"""

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
#
# f = open('test1.txt','a')
# f.write('Fayllar bilan ishlash pythonda muhim qismlardan biri.'
#         'Ayniqsa, web dasturlar bilan ishlashda. ')
# f.close()
#
# f = open('test3.txt','a')
# f.write('Fayllar bilan ishlash pythonda muhim qismlardan biri.'
#         'Ayniqsa, web dasturlar bilan ishlashda. ')
# f.close()


# import os
#
# os.remove('test3.txt')
# print("Fayl muvaffaqiyatli o\'chirildi")


# import os
#
# os.remove('tes.txt')
# print("Fayl muvaffaqiyatli o\'chirildi")
#
# import os
#
# if os.path.exists("test3.txt"):
#         os.remove('test3.txt')
#         print("Fayl muvaffaqiyatli o\'chirildi")
# else:
#         print("Fayl mavjud emas!")


# import os
#
# os.rmdir('hi')
# print("Fayl muvaffaqiyatli o'chirildi")

# with open("test4.txt",'a') as f:
#         f.write('Jahongir')


with open("test4.txt", 'a') as f:
    belgi = True
    while belgi:
        ism = input('Isminigizni kiriting (chiqish = q): ')
        if ism != 'q':
            f.write(f'{ism}\n')
            print("Ismingiz muvaffaqiyatli qo'shildi")
        else:
            belgi = False

with open('test4.txt', 'r') as n:
    print(n.read())
