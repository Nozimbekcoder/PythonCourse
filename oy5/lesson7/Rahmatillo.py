class Avto:
    def __init__(self,model,rang):
        self.model = model
        self.rang = rang


    def malumot(self):
        return f"mashinani {self.model}\n" \
               f"mashina rangi {self.rang}\n"

avto1=Avto('Kia Bomgo','Kok')

class avtomobil(Avto):
    def __init__(self,madel,rang,marka,tezlik,narx):
        super().__init__(madel,rang)

        pass
















