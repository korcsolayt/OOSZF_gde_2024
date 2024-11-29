from datetime import datetime
from classes.szemelyauto import Szemelyauto
from classes.teherauto import Teherauto
from classes.berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []
        self.alap_adatok()

    def alap_adatok(self):
        # Három autó előre betöltése
        self.autok.append(Szemelyauto("AAA-111", "Opel Astra", 5000))
        self.autok.append(Szemelyauto("BBB-222", "Toyota Corolla", 6000))
        self.autok.append(Teherauto("CCC-333", "Mercedes Teherauto", 8000))

        # Négy bérlés előre betöltése
        self.berlesek.append(Berles(self.autok[0], "2024-12-01", "2024-12-05"))
        self.berlesek.append(Berles(self.autok[1], "2024-12-02", "2024-12-04"))
        self.berlesek.append(Berles(self.autok[2], "2024-12-03", "2024-12-06"))
        self.berlesek.append(Berles(self.autok[0], "2024-12-07", "2024-12-10"))

    def ellenoriz_utkozes(self, rendszam, uj_kezdet, uj_veg):
        uj_kezdet = datetime.strptime(uj_kezdet, "%Y-%m-%d")
        uj_veg = datetime.strptime(uj_veg, "%Y-%m-%d")
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                if not (uj_veg < berles.kezdet or uj_kezdet > berles.veg):
                    return True
        return False

    def berles(self, rendszam, kezdet, veg):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                if self.ellenoriz_utkozes(rendszam, kezdet, veg):
                    return "Az autó már foglalt az adott időszakban!"
                uj_berles = Berles(auto, kezdet, veg)
                self.berlesek.append(uj_berles)
                return f"Bérlés sikeres! Ár: {uj_berles.ossz_ar()} Ft"
        return "Nincs ilyen rendszámú autó!"

    def bérlés_lemondása(self, rendszam, kezdet, veg):
        kezdet = datetime.strptime(kezdet, "%Y-%m-%d")
        veg = datetime.strptime(veg, "%Y-%m-%d")
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.kezdet == kezdet and berles.veg == veg:
                self.berlesek.remove(berles)
                return "Bérlés lemondva!"
        return "Nincs ilyen bérlés!"

    def listar_berlesek(self):
        if not self.berlesek:
            return "Nincsenek aktuális bérlések."
        return "\n".join([berles.info() for berles in self.berlesek])

    def listar_autok(self):
        if not self.autok:
            return "Nincsenek autók a rendszerben."
        return "\n".join([auto.info() for auto in self.autok])
