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
        print("lia lia lia, tra lia lia")

    def valgyti(self):
        self.jegos += 10

