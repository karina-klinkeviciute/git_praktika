from mythical import MitineButybe


class cepelinas(MitineButybe):

    def __init__(self, vardas):
        super().__init__(vardas)
        self.jegos = 1

    def keliauti(self, vietove):
        self.vietove = vietove
        self.jegos -= 20

    def valgyti(self):
        self.jegos += 20


cepelinas1 = cepelinas("VirtuBulviu")
cepelinas2 = cepelinas("TarkuotuBulviu")

cepelinas1.dainuoti()
cepelinas2.keliauti("Kaunas")
cepelinas2.valgyti()
cepelinas2.valgyti()
print(cepelinas1.jegos)
print(cepelinas2.vietove)

# Kopija koreguota