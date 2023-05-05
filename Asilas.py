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

    def dainuoti(self):
        print("Unt Sartų unt Sartų lakia roges ratu")


asilas1 = Asilas("Uni")
asilas2 = Asilas("Shiny")

asilas1.dainuoti()
asilas2.keliauti("Unt Utenų")
asilas2.valgyti()
asilas2.valgyti()
print(asilas2.jegos)
print(asilas2.vietove)
