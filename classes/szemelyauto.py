from classes.auto import Auto

class Szemelyauto(Auto):
    def info(self):
        return f"Személyautó: {self.rendszam}, {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap"
