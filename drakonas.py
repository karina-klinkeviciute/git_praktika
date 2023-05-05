from mythical import MitineButybe


class Drakonas(MitineButybe):

    def __init__(self, vardas):
        super().__init__(vardas)
        self.jegos = 1000

    def keliauti(self, vietove):
        self.vietove = vietove
        self.jegos -= 200

    def valgyti(self):
        self.jegos += 2000


Drakonas1 = Drakonas("Unri")
Drakonas2 = Drakonas("Shinry")
Drakonas3 = Drakonas("Kivi")

Drakonas1.dainuoti()
Drakonas2.keliauti("Kaunas")
Drakonas1.keliauti("Vilnius")
Drakonas3.keliauti("Klaipeda")
print(Drakonas2.jegos)
Drakonas2.valgyti()
Drakonas2.valgyti()
print(Drakonas2.jegos)
print(Drakonas2.vietove)
