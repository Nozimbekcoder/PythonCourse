# 1. Berilgan x-y+q*a  ni hisoblovchi lambda funksiyasini yozing.
#
# a= lambda x,y,q,a: x-y+q*a
# print(a(2,3,4,8))

# 2. Berilgan x-y+q*a  ni hisoblovchi funksiyasini yozing.

# def form(x,y,q,a):
#     return x-y+q*a
#
# print(form(1,2,3,4))
#

# 3. 1-999 oraliqdagi sonlar berilgan. Berilgan sonni
# ikki xonali juft son, uch xonali toq son va x.k.
# ekranga yozadigan dastur tuzing.

# belgi = True
# while belgi:
#     son = input('1-999 gacha son kiriting: ')
#     if son != 'q':
#         if (int(son)) % 2 == 0:
#             print(f"{len(son)} xonali Juft son")
#         elif (int(son)) % 2 != 0:
#             print(f"{len(son)} xonali Toq son")
#     else:
#         belgi = False
#         print("Dastur Yakunlandi.")


# 4. Foydalanuvchidan ismi, familiyasini, tel raqamini sorab har bir foydalanuvchini
# malumotlarini saqlab olish uchun dastur tuzing.
# Dastur q harfi kiritilgan holda, tugatilsin aks holda keyingi malumotlarni
# qabul qilib olish uchun davom eting.
# Ma'lumotlarni txt faylga yozib
# oling dastur tugatilgach uni konsolda korsating.

def kirit(matn):
    return input(matn)


over = True

while over:
    yana = kirit("Ma'lumot qo'shasizmi?(tugatish 'q'): ")
    if yana != 'q':
        ism = input("Ismingiz: ").title()
        fam = input("Familyangiz: ").title()
        tel = kirit("Telefon raqamingiz(93 057 66 03): ")
        with open('./royhat.txt', 'a') as f:
            f.write(f'\n'
                    f'Ismingiz: {ism}\n'
                    f'Familyangiz: {fam}\n'
                    f'Telefon raqamingiz: +998 {tel}\n'
                    f'----------------------------------------------------\n')
        print("Ma'lumotlar muvaffaqiyatli saqlandi!\n")

    else:
        over = False
        print('Dastur Yakunlandi')
        with open('./royhat.txt', 'r') as f:
            print(f.read())

input()



# 5. pyinstaller kutubxonasi yordamida biror 4 masaladagi dasturni exe faylga aylantiring.
#
# cmd yoki powershell dan fayl joylashgan joyga kelib
#
# pyinstaller --onefile <faylnomi>.py va Enter tugmasi bosiladi