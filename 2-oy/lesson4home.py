# Taklifnoma Vazifasi
#
# mehmonlar = ['Ali', 'Vali', 'Abdusamad', 'Tesha']
# mehmonlar = []
# nomasoni = input('Nechta taklifnoma kerak? >>> ')
# if nomasoni.isdigit():
#     nomasoni = int(nomasoni)
#     if nomasoni > 0:
#         for ism in range(nomasoni):
#             ismlar = input(f'{ism + 1}-Do\'stingizni ismini kiriting: ')
#             mehmonlar.append(ismlar)
#
#         mehmonlarroyhati = []
#         for mehmon in mehmonlar:
#             mehmonlarroyhati.append(mehmon)
#         print(mehmonlarroyhati)
#     else:
#         print('Taklifnoma yozish uchun kamida 1ta mehmon bolish kerak!')
# else:
#     print(f'Siz mehmonlar sonini kiritmadingiz!')


mehmonlar = []
nomasoni= input('Taklifnomalar sonini kiriting: ')
if nomasoni.isdigit():
    nomasoni=int(nomasoni)
    if nomasoni>0:
        for son in range(nomasoni):
            ism=input(f'{son+1}-Do\'stingizni ismini kiriting: ')
            mehmonlar.append(ism)
            print(mehmonlar)
    else:
        print('Siz kamida bitta mehmon taklif qilishingiz kerak!')
else:
    print('yoki Siz raqam kiritmadingiz!')












# oylar = ('Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr')
# sana = input('Sanani kiriting: ')
# if sana.isdigit():
#     kun = int(sana)
#     if kun > 0 and kun <= 31:
#         oy = input('Oyni kiriting: ').title()
#         if (oy in oylar) or (oy.isdigit()):
#             if oy.isdigit():
#                 oy = int(oy)
#                 if oy <= 12 and oy > 0:
#                     oynomi = oylar[oy - 1]
#                     for mehmon in mehmonlar:
#                         print(
#                             f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
#                             f'Xurmat bilan Palonchiyevlar oilasi\n')
#
#                 else:
#                     print('Kechirasiz siz kiritgan ma\'lumotlar not\'og\'ri!!!')
#             elif not (oy.isdigit()):
#                 for mehmon in mehmonlar:
#                     print(
#                         f'Hurmatli {mehmon}, Sizni {sana}-{oy} kuni nahorgi oshga taklif etamiz\n'
#                         f'Xurmat bilan Palonchiyevlar oilasi\n')
#         else:
#             print('Kechirasiz siz kiritgan ma\'lumotlar not\'og\'ri!!!')
#     else:
#         print('Kechirasiz siz kiritgan Sana not\'og\'ri!!!')
# else:
#     print('Kechirasiz sana faqat raqamlarda qabul qilinadi!!!')
