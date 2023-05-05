from mythical import MitineButybe

class Beragis(MitineButybe):
    def __init__(self, vardas):
        super().__init__(vardas)
        self.pinigai = 1000

    def keliauti(self, vietove):
        self.vietove = vietove

    def valgyti(self):
        self.pinigai += 20

    def miegoti(self, miegoti):
        self.miegoti = miegoti
        self.miegoti = "As miegu ko nori?"

    def dainuoti(self):
        print("Miau Miau Au Au")

Beragis.dainuoti("Dainuok")
beragis = Beragis("Markas")
beragis.keliauti("Vilnius")
beragis.miegoti("Miegok")


print(f"Duok man",beragis.pinigai,"Eu", "!!!")
print(f"Mano miestas",beragis.vietove)
print(f"Nemaišyk man!" ,beragis.miegoti)