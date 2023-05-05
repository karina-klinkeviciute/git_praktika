from mythical import MitineButybe


class Vandenis(MitineButybe):

    def __init__(self, vardas):
        super().__init__(vardas)
        self.jegos = 800

    def keliauti(self, vietove):
        self.vietove = vietove
        self.jegos -= 50

    def valgyti(self):
        self.jegos += 30


Vandeninis1 = Vandenis("Uni")
Vandeninis2 = Vandenis("Shiny")

Vandeninis1.dainuoti()
Vandeninis2.keliauti("Vilnius")
Vandeninis1.valgyti()
Vandeninis2.valgyti()
print(Vandeninis1.jegos)
print(Vandeninis2.vietove)
