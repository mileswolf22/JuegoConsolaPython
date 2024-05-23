from VJ_TRY.Clases_y_Personajes.Personaje import Personaje

import time
import sys
import numpy as np

from VJ_TRY.Tablero_y_Menus import Menus

tablero = Menus()

personaje = Personaje(
    clase="",
    hp=0,
    mp=0,
    ataque=0,
    defensa=0,
    defensa_magica=0,
    magia=0,
    resistencia=0,
    suerte=0,
    inteligencia=0,
    carisma=0,
    taza_de_crecimiento_magico=0,
    taza_de_aprendizaje=0
)


def imprimir_menu():
    print("\n¡Bienvenido al juego RPG!")
    print("1. Comenzar nueva partida")
    print("2. Cargar partida guardada")
    print("3. Configuración")
    print("4. Salir del juego")


def animacion_cargando():
    print("Cargando...")
    for _ in range(5):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print("\n¡Listo!\n")


def configuracion():
    print("\nConfiguración:")
    print("1. Cambiar idioma")
    print("2. Ajustar volumen")
    print("3. Volver al menú principal")


def menu():
    while True:
        imprimir_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\n¡Preparándose para la aventura!")
            animacion_cargando()
            personaje.crear_personaje()
            matriz = np.array([["[  ]" for _ in range(10)] for _ in range(10)])
            tablero.crear_mapa(matriz)

            #Elegir el tipo de partida

            # Lógica para comenzar una nueva partida
        elif opcion == "2":
            print("\nCargando partida guardada...")
            animacion_cargando()
            # Lógica para cargar partida guardada
        elif opcion == "3":
            while True:
                configuracion()
                opcion_config = input("Selecciona una opción de configuración: ")
                if opcion_config == "1":
                    print("\nIdioma cambiado.")
                    # Lógica para cambiar idioma
                elif opcion_config == "2":
                    print("\nVolumen ajustado.")
                    # Lógica para ajustar volumen
                elif opcion_config == "3":
                    break
                else:
                    print("Opción inválida. Inténtalo de nuevo.")
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()
