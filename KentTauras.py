from mythical import MitineButybe


class KentTauras(MitineButybe):

    def __init__(self, vardas):
        super().__init__(vardas)
        self.jegos = 9000

    def keliauti(self, vietove):
        self.vietove = vietove
        self.jegos -= 20

    def valgyti(self):
        self.jegos += 20


KentTauras1 = KentTauras("Vova")
KentTauras2 = KentTauras("Zene")

KentTauras1.dainuoti()
KentTauras2.keliauti("Salūnas")
KentTauras1.keliauti("Salūnas")
KentTauras1.valgyti()
KentTauras2.valgyti()
print(KentTauras1.jegos)
print(KentTauras1.vietove)
print(KentTauras2.jegos)
print(KentTauras2.vietove)
