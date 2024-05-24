from VJ_TRY.Clases_y_Personajes.Personaje import Personaje
from VJ_TRY.Cargar_Guardar.Juego import Juego
from VJ_TRY.Clases_y_Personajes.Mochila import Mochila
import time
import sys
import numpy as np

from VJ_TRY.Tablero_y_Menus import Menus

tablero = Menus()
juego = Juego
mochi = Mochila

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
    taza_de_aprendizaje=0,
    posicion=[0, 0]
)


def imprimir_menu():
    print("\n¡Bienvenido al juego RPG!")
    print("1. Comenzar nueva partida")
    print("2. Cargar partida guardada")
    print("4. Salir del juego")


def animacion_cargando():
    print("Cargando...")
    for _ in range(5):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print("\n¡Listo!\n")


def menu():
    while True:
        imprimir_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\n¡Preparándose para la aventura!")
            animacion_cargando()
            id_persona = personaje.crear_personaje()
            matriz = np.array([["[  ]" for _ in range(10)] for _ in range(10)])
            table = tablero.crear_mapa(matriz)
            posicion_jugador = id_persona[1]  # Tomo el elemento interno de la posicion [0][0] de la matriz
            posicion_anterior = posicion_jugador  # Para saber que habia antes de JG
            cont_pos_ant = table[0][0]
            table[0][0] = "[JG]"  # A partir de aqui la posicion [0][0] es sustiduida por JG
            new_posicion_jugador = table[0][0]  # Nueva marca cuando jugador se posicione
            print(f"Elemento en Posicion ={posicion_jugador}")  # Elemento existente previo al cambio JG
            print(f"Posicion anterior ={posicion_anterior}")  # Indicar el elemento anterior para el juego
            print(f"Posicion nueva ={new_posicion_jugador}")  # Nueva posicion indicada por JG
            # Elegir el tipo de partida

            # Encerrar esto en una bucle, el bucle terminara cuando la vida del jugador sea 0
            mochila_persona = mochi.crear_mochila(id_persona[0])
            juego.menu_juego(id_persona, table, mochila_persona, posicion_anterior, new_posicion_jugador, cont_pos_ant)

            # Lógica para comenzar una nueva partida
        elif opcion == "2":
            print("\nCargando partida guardada...")
            animacion_cargando()
            # Lógica para cargar partida guardada

        elif opcion == "3":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()
