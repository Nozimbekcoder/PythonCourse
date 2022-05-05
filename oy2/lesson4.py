"""
Mavzu: Loop (tsikllar) pythonda for takrorlansh operatori
"""
# a = 10
# b = 'ruchka'

# for x in 'salom':
#     print('salom')


# mevalar = ['olma', 'shaftoli', 'kivi', 'banan']

# for meva in mevalar:
#     print(meva.title())
#
# for meva in mevalar:
#     print(meva.upper())

# for ixtiyoriy_uzgaruvchi in mevalar:
#     print('salom')

# for i in range(1,11,2):
#     print(i)

# Assalomu alaykum ALI
# Assalomu alaykum VALI

# karra=int(input('Nechi karra kerak?  >>>'))
# for son1 in range(1,11):
#     print(f'{karra} * {son1} = {karra*son1}')
#
# karra=int(input('Nechi karra kerak?  >>>'))
# sum = [1,6,9,5,88,77,45,998]
# for son1 in sum:
#     print(f'{karra} * {son1} = {karra*son1}')















# Taklifnoma Vazifasi

mehmonlar = ['Ali', 'Vali', 'Abdusamad', 'Teshavoy']
# mehmonlar = []
# nomasoni = int(input('Nechta taklifnoma kerak? >>> '))

# for ism in range(nomasoni):
#     ismlar = input(f'{ism + 1}-Do\'stingizni ismini kiriting: ')
#     mehmonlar.append(ismlar)

# for mehmon in mehmonlar:
#     print(mehmon)

oylar = ('Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr')
sana = int(input('Sanani kiriting: '))
oy = input('Oyni kiriting: ').title()
if (oy in oylar) or (oy.isdigit()):
    if oy.isdigit():
        oy = int(oy)
        if oy == 1:
            oynomi = oylar[0]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 2:
            oynomi = oylar[1]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 3:
            oynomi = oylar[2]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 4:
            oynomi = oylar[3]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 5:
            oynomi = oylar[4]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 6:
            oynomi = oylar[5]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 7:
            oynomi = oylar[6]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 8:
            oynomi = oylar[7]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 9:
            oynomi = oylar[8]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 10:
            oynomi = oylar[9]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 11:
            oynomi = oylar[10]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')
        elif oy == 12:
            oynomi = oylar[oy-1]
            for mehmon in mehmonlar:
                print(
                    f'Hurmatli {mehmon}, Sizni {sana}-{oynomi} kuni nahorgi oshga taklif etamiz\n'
                    f'Xurmat bilan Palonchiyevlar oilasi\n')

        elif oy <= 12 and oy > 0:
            print('Kechirasiz siz kiritgan ma\'lumotlar not\'og\'ri!!')

        else:
            print('Kechirasiz siz kiritgan ma\'lumotlar not\'og\'ri!!')
else:
    print('Kechirasiz siz kiritgan ma\'lumotlar not\'og\'ri!!')
