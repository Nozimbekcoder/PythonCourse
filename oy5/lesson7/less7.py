# """
# lesson7
#
# Mavzu: Super class va Voris class tushuncha , qo'llab korish , amaliyot qilish
#
# """
#
#
# # class Shaxs:
# #     """
# #     Shaxs class
# #     """
# #     def __init__(self, ism,familya, tyil):
# #         self.ism = ism
# #         self.familya = familya
# #         self.tyil = tyil
# #
# #     def __str__(self):
# #         return f"{self.familya} {self.ism}"
# #
# #     def get_info(self):
# #         return f"Shaxs {self.familya} {self.ism}\n" \
# #                f"Tug'ilgan yili {self.tyil}"
# #
# #     def get_yosh(self, hyil=2022):
# #         return hyil - self.tyil
# #
# #
# #
# # class Student(Shaxs):
# #     def __init__(self,ism, familya, tyil,kurs, otm):
# #         super().__init__(ism,familya, tyil)
# #         self.kurs = kurs
# #         self.otm = otm
# #
# #     def get_malumot(self):
# #         return f"Shaxs {self.familya} {self.ism}\n" \
# #                 f"Tug'ilgan yili {self.tyil}\n" \
# #                f"Kursi {self.kurs}\n" \
# #                f"Oliy ta'lim Muassasasi : {self.otm}"
# #
# #
# # odam1 = Shaxs('Hojiakbar','Rahimov',2006)
# # talaba1= Student('Hojiakbar','Rahimov',2006,2,'NamDU')
# #
# #
# class Avto():
#     def __init__(self, rang, model):
#         self.rang = rang
#         self.model = model
#
#     def malumot(self):
#         return f"mashinani {self.model}\n mashina rangi {self.rang}\n"
#
#
# # avto1 = Avto('Kia Bomgo', 'Kok')
# # avto2 = Avto('w Bomgo', 'Kok')
# # avto3 = Avto('a Bomgo', 'Kok')
# # avto4 = Avto('q Bomgo', 'Kok')
#
#
# # from Rahmatillo import Avto
#
# class Uni(Avto):
#     def ___init__(self, rang, model, yil):
#         super().__init__(rang, model)
#         self.yil = yil
#
#     # def get_malumot(self):
#     #     a=f"Marka: {self.rang} Model: {self.model} yil {self.yil}"
#     #     return a
#
# u1 = Uni()
# # # u2 = Uni('nexia', 'oq')


class Avto:
    def __init__(self, model, rang):
        self.model = model
        self.rang = rang

    def malumot(self):
        return f"mashina modeli {self.model} \n mashina rangi {self.rang} \n"


class Uni(Avto):
    def __init__(self, model, rang, yil, kuzov):
        super().__init__(model, rang)
        self.yil = yil
        self.kuzov = kuzov

    def malumot(self):
        return f"mashina modeli {self.model} \n mashina rangi {self.rang}\n" \
               f"mashina yili {self.yil} \n mashina kuzov {self.kuzov} \n"



