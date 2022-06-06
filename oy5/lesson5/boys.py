"""
lesson 4
Python OOP dasturlash
OOP - Object Oriented Programming
Obyektlar bilan ishlash,

"""
# class Talaba():
#     def __init__(self,ism,familya,tyil):
#
#         self.ism=ism
#         self.familya=familya
#         self.tyil = tyil
#
#     def yosh(self,yili):
#         return yili-self.tyil
#
#     def name(self):
#         return self.ism
#
#     def familya(self):
#         return self.familya
#
#     def tyil(self):
#         return self.tyil
#
#talaba1=Talaba("Abror","Hasanov",2003)


class avtomabil:
    def __init__(self,rang,tezlik,narx):

        self.rang=rang
        self.tezlik=tezlik
        self.narx=narx


    def avto(self):

        return f"mashina rangi {self.rang}\n" \
        f"mashina tezlik {self.tezlik}\n" \
        f"narxi {self.narx}"

avtomi=avtomabil("qora","260km","2000$")


print(avtomi.avto())

