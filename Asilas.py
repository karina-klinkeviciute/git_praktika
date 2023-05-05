from mythical import MitineButybe


class Asilas(MitineButybe):

    def __init__(self, vardas):
        super().__init__(vardas)
        self.jegos = 1000

    def keliauti(self, vietove):
        self.vietove = vietove
        self.jegos -= 20

    def valgyti(self):
        self.jegos += 20


vienaragis1 = Asilas("Uni")
vienaragis2 = Asilas("Shiny")

vienaragis1.dainuoti()
vienaragis2.keliauti("Kaunas")
vienaragis2.valgyti()
vienaragis2.valgyti()
print(vienaragis2.jegos)
print(vienaragis2.vietove)
