from mythical import MitineButybe


class Pegasas(MitineButybe):

    def __init__(self, vardas):
        super().__init__(vardas)
        self.jegos = 2000

    def keliauti(self, vietove):
        self.vietove = vietove
        self.jegos -= 20

    def valgyti(self):
        self.jegos += 20


pegasas1 = Pegasas("Peg")
pegasas2 = Pegasas("Shiny pink")

pegasas1.dainuoti()
pegasas2.keliauti("Kaunas")
print(pegasas1.jegos)
pegasas2.valgyti()
pegasas2.valgyti()
print(pegasas2.jegos)
print(pegasas22.vietove)
