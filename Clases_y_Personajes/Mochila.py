class Mochila:
    # Evito el uso de init por que no sera necesario llenar todos los campos en cada
    # instancia de la mochila, sino unicamente los campos requeridos segun sean
    # las necesidades
    @staticmethod
    def crear_mochila(id):
        mochila = {
            id: {
                "Equipables": {
                    "Armas": {
                        "Espadas": [],
                        "Lanzas": [],
                        "Daga": [],
                        "Arco": [],
                        "Guantes": [],
                        "Vara": [],
                        "Cetro": [],
                        "Escudo": []
                    },
                    "Armaduras": {
                        "Yelmo": [],
                        "Pechera": [],
                        "Pantalon": [],
                        "Zapato": [],
                        "Anillo": [],
                        "Collar": []
                    }
                },
                "Consumibles": {
                    "Pocion": [],
                    "Pergaminos": []
                },
                "Objetos": {},
                "ObjetosEspeciales": {}
            }
        }
        return mochila

    @staticmethod
    def mostrar_inventario(id_user, mochi):
        global armas_disponibles
        print("----------------Mochila--------------------")
        print("1. Armas \t 2. Armaduras")
        print("3. Consumibles \t 4. Objetos")

        seccion = int(input("Seccion: "))
        print("\n")
        if seccion == 1:
            print("-------Armas-------")
            print("1. Espadas \t 5. Guantes")
            print("2. Lanzas \t 6. Varas")
            print("3. Dagas \t 7. Cetros")
            print("4. Arcos \t 8. Escudos")
            agregar_espada = mochi[id_user]["Equipables"]["Armas"]["Espadas"]
            agregar_espada.append("Espada de Madera")
            agregar_espada.append("Espada de Hierro")
            agregar_espada.append("Espada de Acero")

            armas = mochi[id_user]["Equipables"]["Armas"]
            espadas = armas.get("Espadas")
            lanzas = armas.get("Lanzas")
            daga = armas.get("Daga")
            arco = armas.get("Arco")
            guantes = armas.get("Guantes")
            vara = armas.get("Vara")
            cetro = armas.get("Cetro")
            escudo = armas.get("Escudo")
            armas_disponibles = {
                1: espadas,
                2: lanzas,
                3: daga,
                4: arco,
                5: guantes,
                6: vara,
                7: cetro,
                8: escudo
            }

        seccion_armas = int(input("Arma a consultar: "))
        print("\n")
        contador = 0
        if seccion_armas in armas_disponibles:
            if not armas_disponibles[seccion_armas]:
                print(f"Vacio")
            else:
                print(f"--------Contenido------------")
                for espada in armas_disponibles[seccion_armas]:
                    contador += 1
                    print(f"[{contador}] {espada}")

                print("Que deseas hacer?: ")
            print("Volver [V]")

        elif seccion == 2:
            print("-------Armaduras-------")
            pass
        elif seccion == 3:
            print("-------Consumibles-------")
            pass
        elif seccion == 4:
            print("------Objetos-------")