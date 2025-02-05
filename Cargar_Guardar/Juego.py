from VJ_TRY.Tablero_y_Menus import Menus
from VJ_TRY.Clases_y_Personajes.Personaje import Personaje
from VJ_TRY.Clases_y_Personajes import Enemigo
from VJ_TRY.Clases_y_Personajes.Mochila import Mochila

from VJ_TRY.ataques import Armas
from VJ_TRY.ataques import Batallas

persona = Personaje(
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
    posicion=(0, 0)
)

menu = Menus()
dado = Menus()
mochi = Mochila



class Juego:
    def __init__(self, personaje, tablero):
        self.personaje = personaje
        self.tablero = tablero

    @staticmethod
    # Cuando sea la primera vez jugando
    def comenzar_juego(jugador, tablero):
        table = tablero
        # Codigo para mostar una situacion al jugador

    @staticmethod
    def cargar_juego():
        pass

    @staticmethod
    def guardar_juego():
        pass

    @staticmethod
    def pausa():
        pass

    @staticmethod
    def partida_cueva():
        pass

    @staticmethod
    def menu_juego(id_, matriz, mochila, ant_posicion, new_posicion, contenido_ant):
        print("-------------Aventura-------------")
        print("----Cual es tu proxima accion?----")
        print("1. Tirar dados \t 3. Mochila")
        print("2. Ver mapa \t 4. Ver estadisticas")
        print("5. Guardar y salir")
        accion = int(input("seleccion: "))

        if accion == 1:
            dados = dado.lanzar_dado
            menu.ver_mapa(matriz)
            movimiento = input("Hacia donde deseas moverte?\n \tW\nA   S   D\n Seleccion: ")
            resultado = menu.avanzar_tablero(matriz, ant_posicion, new_posicion, movimiento, dados[1], contenido_ant)
            menu.ver_mapa(matriz)
            menu.verificar_casilla(resultado[1])
            print(resultado[0])
        elif accion == 2:
            menu.ver_mapa(matriz)

        elif accion == 3:
            mochi.mostrar_inventario(id_, mochila)
        elif accion == 4:
            pass
        elif accion == 5:
            pass

