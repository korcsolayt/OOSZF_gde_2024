from datetime import datetime

class Berles:
    def __init__(self, auto, kezdet, veg):
        self.auto = auto
        self.kezdet = datetime.strptime(kezdet, "%Y-%m-%d")
        self.veg = datetime.strptime(veg, "%Y-%m-%d")

    def napok_szama(self):
        return (self.veg - self.kezdet).days + 1

    def ossz_ar(self):
        return self.auto.berleti_dij * self.napok_szama()

    def info(self):
        return (f"Autó: {self.auto.rendszam}, Típus: {self.auto.tipus}, "
                f"Kezdet: {self.kezdet.strftime('%Y-%m-%d')}, Vég: {self.veg.strftime('%Y-%m-%d')}, "
                f"Napok száma: {self.napok_szama()}, Összesen: {self.ossz_ar()} Ft")
