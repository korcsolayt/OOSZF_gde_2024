from classes.autokolcsonzo import Autokolcsonzo

def main():
    kolcsonzo = Autokolcsonzo("City Rent")

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ RENDSZER ---")
        print("1. Autók listázása")
        print("2. Autó bérlése")
        print("3. Bérlés lemondása")
        print("4. Aktuális bérlések listázása")
        print("0. Kilépés")
        valasz = input("Válassz egy opciót: ")

        if valasz == "1":
            print("\nElérhető autók:")
            print(kolcsonzo.listar_autok())

        elif valasz == "2":
            rendszam = input("Add meg a rendszámot: ")
            kezdet = input("Add meg a kezdő dátumot (YYYY-MM-DD): ")
            veg = input("Add meg a vég dátumot (YYYY-MM-DD): ")
            print(kolcsonzo.berles(rendszam, kezdet, veg))

        elif valasz == "3":
            rendszam = input("Add meg a rendszámot: ")
            kezdet = input("Add meg a kezdő dátumot (YYYY-MM-DD): ")
            veg = input("Add meg a vég dátumot (YYYY-MM-DD): ")
            print(kolcsonzo.bérlés_lemondása(rendszam, kezdet, veg))

        elif valasz == "4":
            print("\nAktuális bérlések:")
            print(kolcsonzo.listar_berlesek())

        elif valasz == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen opció. Próbáld újra!")

if __name__ == "__main__":
    main()
