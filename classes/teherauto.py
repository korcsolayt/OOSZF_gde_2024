from classes.auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)

    def info(self):
        return f"Teherautó: {self.rendszam}, {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap"
