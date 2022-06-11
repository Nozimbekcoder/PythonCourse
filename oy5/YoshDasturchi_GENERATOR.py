import random

oquvchilar = ['Rahimov Hojiakbar',
              'Rashidov Rahmatillo',
              'Madaminov Abdurauf',
              'Sherzodjanov Abdulaziz',
              'Hasanboyev Mirziyo'
]
s=True
while s:
    n1 = random.choice(oquvchilar)
    n2 = random.choice(oquvchilar)
    while n1!=n2:
        print(f'Dars tushuntiruvchi o\'uvchi bu\n'
              f'1-  {n1}\n'
              f'2-  {n2}.')

        s=False
        break
