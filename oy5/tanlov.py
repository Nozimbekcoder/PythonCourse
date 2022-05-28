import random

oquvchilar = ['Rahimov Hojiakbar',
              'Madaminov Abdurauf',
              'Sherzodjanov Abdulaziz',
              'Hasanboyev Mirziyo',
              'Rashidov Rahmatillo'
]

n1 = random.choice(oquvchilar)
n2 = random.choice(oquvchilar)
while n1!=n2:
    print(f'Dars tushuntiruvchi o\'uvchi bu\n'
          f'1-  {n1}\n'
          f'2-  {n2}.')
    if n1!=n2:
        break