import random

oquvchilar = ['Rahimov Hojiakbar',
              'Madaminov Abdurauf',
              'Sherzodjanov Abdulaziz',
              'Hasanboyev Mirziyo',
              'Rashidov Rahmatillo'
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
#
# from tkinter import*
#
# root =Tk()
# window_width = 800
# window_height = 400
# # get the screen dimension
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# # find the center point
# center_x = int(screen_width / 2 - window_width / 2)
# center_y = int(screen_height / 2 - window_height / 2)
#
# # set the position of the window to the center of the screen
# root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# root.resizable(width=False, height=False)
#
#
#
#
# root.mainloop()