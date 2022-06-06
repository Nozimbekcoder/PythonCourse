class Talaba:
    def __init__(self,ism,familya,tyil):

        self.ism=ism
        self.familya=familya
        self.tyil=tyil

    def get_info(self):
        info=f"Talabani ismi {self.ism},Familyasi {self.familya}" \
             f"Tugilgan yili {self.tyil}"

        return self.get_info

    def age(self,yil):
        return yil-self.tyil

class Shaxs(Talaba):
    def __init__(self,ism,familya,tyil,passport):
        super().__init__(ism,familya,tyil)

        self.passport=passport

    def get(self):
        odam=f"Ismi {self.ism},Familyasi {self.familya}" \
             f"Tugilgan yili {self.tyil},Passport : {self.passport}"

        return self.get

talaba1=Shaxs("Abror","Axrorov",'2009',"Q1222222k")
talaba