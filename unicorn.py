from mythical import MitineButybe


class slibinas(MitineButybe):

    def __init__(self, vardas):
        super().__init__(vardas)
        self.jegos = "ugnis"

    def keliauti(self, vietove):
        self.vietove = vietove
        self.jegos = "zaibai"
    def dainuoti(self):
        print("HARRRR!!!!! HARRRRR!!!!")


slibinas1 = slibinas("zvynas")
slibinas2 = slibinas("zvynuotas")

slibinas1.dainuoti()
slibinas2.keliauti("kalnai ir uolos")

print(slibinas2.jegos)
print(slibinas2.vietove)
