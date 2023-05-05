from mythical import MitineButybe


class Vienaragis(MitineButybe):

    def __init__(self, vardas):
        super().__init__(vardas)
        self.jegos = 1000

    def keliauti(self, vietove):
        self.vietove = vietove
        self.jegos -= 20

    def valgyti(self):
        self.jegos += 20


vienaragis1 = Vienaragis("Uni")
vienaragis2 = Vienaragis("Shiny")

vienaragis1.dainuoti()
vienaragis2.keliauti("Kaunas")
print(vienaragis2.jegos)
vienaragis2.valgyti()
vienaragis2.valgyti()
print(vienaragis2.jegos)
print(vienaragis2.vietove)
