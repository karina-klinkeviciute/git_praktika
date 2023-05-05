class MitineButybe:
    def __init__(self, vardas):
        self.vardas = vardas
        self.amzius = 0
        self.vietove = None
        self.jegos = 100

    def keliauti(self, vietove):
        self.vietove = vietove
        self.jegos -= 10

    def dainuoti(self):
        print("Unt Sartų unt Sartų lakia roges ratu")

    def valgyti(self):
        self.jegos += 10

