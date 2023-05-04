class Darboviete:
    def __init__(self, pavadinimas):
        self.pavadinimas = pavadinimas
        self.darbo_pradzia = 8
        self.darbo_pabaiga = 17
        self.ar_dirba = False
        self.visi_kontaktai = {}

    def keisti_darbo_valandas(self, pradzia, pabaiga):
        self.darbo_pradzia = pradzia
        self.darbo_pabaiga = pabaiga

    def kaip_dirba(self):
        print(f"Mes dirbam nuo {self.darbo_pradzia} iki {self.darbo_pabaiga}")

    def pradeti_dirbti(self):
        self.ar_dirba = True

    def baigti_dirbti(self):
        self.ar_dirba = False

    def ka_daro(self):
        print("Ši įmonė nedaro nieko")

    def prideti_kontaktus(self, adresas = None, telefonas = None, email = None):
        self.visi_kontaktai["adresas"] = adresas
        self.visi_kontaktai["telefonas"] = telefonas
        self.visi_kontaktai["email"] = email

    def kontaktai(self):
        for kontaktas, reiksme in self.visi_kontaktai.items():
            print(f"Mūsų {kontaktas}: {reiksme}")