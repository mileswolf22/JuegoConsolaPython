from VJ_TRY.Tablero_y_Menus import Menus
from VJ_TRY.Clases_y_Personajes.Personaje import Personaje
from VJ_TRY.Clases_y_Personajes import Enemigo
from VJ_TRY.Clases_y_Personajes.Mochila import  Mochila
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
    taza_de_aprendizaje=0
)

menu = Menus
mochi = Mochila


class Juego:
    def __init__(self, personaje, tablero):
        self.personaje = personaje
        self.tablero = tablero

    @staticmethod
    # Cuando sea la primera vez jugando
    def comenzar_juego(jugador, tablero):
        table = tablero
        #Codigo para mostar una situacion al jugador


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
    def menu_juego(id_, matriz, mochila):
        print("-------------Menu-------------")
        print("-----Que es lo que deseas-----")
        print("1. Ver estadisticas \t 3. Mochila")
        print("2. Ver Mapa \t 4. Guardar y salir")
        accion = int(input("seleccion: "))

        if accion == 1:
            persona.mostrar_jugador(id_)
        elif accion == 2:
            menu.ver_mapa(matriz)
        elif accion == 3:
            mochi.mostrar_inventario(id_, mochila)
        elif accion == 4:
            pass
