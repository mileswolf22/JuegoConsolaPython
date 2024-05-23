from VJ_TRY.Clases_y_Personajes.Clases import *
from random import randint
from VJ_TRY.Clases_y_Personajes.Mochila import *
from VJ_TRY.Clases_y_Personajes.Clases import Guerrero
from VJ_TRY.Clases_y_Personajes.Clases import Ladron
from VJ_TRY.Clases_y_Personajes.Clases import Cazador
from VJ_TRY.Clases_y_Personajes.Clases import Clerigo
from VJ_TRY.Clases_y_Personajes.Clases import Paladin
from VJ_TRY.Clases_y_Personajes.Clases import Barbaro
from VJ_TRY.Clases_y_Personajes.Clases import Mago_Blanco
from VJ_TRY.Clases_y_Personajes.Clases import Mago_Oscuro

# Se inicializa diccionario vacio de jugadores
jugadores = {}
contador_jugadores = 0
guerrero = Guerrero()
ladron = Ladron()
cazador = Cazador()
clerigo = Clerigo()
paladin = Paladin()
barbaro = Barbaro()
mago_Blanco = Mago_Blanco()
mago_Oscuro = Mago_Oscuro()
Mochila = Mochila


class Personaje(Clases):
    def __init__(self, hp, mp, ataque, defensa, defensa_magica, magia, resistencia, suerte, inteligencia, carisma,
                 taza_de_crecimiento_magico, taza_de_aprendizaje, id_player=0, nombre="", nickname="", clase="",
                 nivel=0, experiencia=0, equipo_arma=None, equipo_armadura=None, mochila=None):

        super().__init__(
            clase=clase,
            hp=hp,
            mp=mp,
            ataque=ataque,
            defensa=defensa,
            defensa_magica=defensa_magica,
            magia=magia,
            resistencia=resistencia,
            suerte=suerte,
            inteligencia=inteligencia,
            carisma=carisma,
            taza_de_crecimiento_magico=taza_de_crecimiento_magico,
            taza_de_aprendizaje=taza_de_aprendizaje
        )

        self.id_player = id_player
        self.id_player = id_player
        self.nombre = nombre
        self.nickname = nickname
        self.clase = clase
        self.nivel = nivel
        self.experiencia = experiencia
        self.equipo_arma = equipo_arma if equipo_arma is not None else []
        self.equipo_armadura = equipo_armadura if equipo_armadura is not None else []
        self.mochila = mochila if mochila is not None else Mochila.crear_mochila(self.id_player)

    def crear_personaje(self):
        # Generacion de id
        self.id_player = randint(1, 1000)

        global contador_jugadores
        nombre_personaje = input("Nombre de partida: ")
        self.nombre = nombre_personaje

        nickname_personaje = input("Nombra a tu Heroe: ")
        self.nickname = nickname_personaje

        print("Clases: ")
        print("\t\tGuerrero[1]")
        print("\t\tMago Blanco[2]")
        print("\t\tMago Oscuro[3]")
        print("\t\tLadron[4]")
        print("\t\tCazador[5]")
        print("\t\tClerigo[6]")
        print("\t\tPaladin[7]")
        print("\t\tBarbaro[8]")
        clase_personaje = int(input("Elije tu clase: "))
        # Diccionario que guarda las opciones disponibles
        # Esto me ahorro hacer un if/elif entre cada una de las opciones
        clase_metodos = {
            1: guerrero,
            2: mago_Blanco,
            3: mago_Oscuro,
            4: ladron,
            5: cazador,
            6: clerigo,
            7: paladin,
            8: barbaro
        }
        # Se verifica que clase personajes coincida con alguno de los elementos dentro de clase_metodos
        # Recodar que 1 toma el valor de la clave
        # Si el usuario digita "1" el codigo verificara que este "1" este en el clase_metodos
        if clase_personaje in clase_metodos:
            print(f"\t\n---!!!Binvenido {self.nickname} el {clase_metodos[clase_personaje].clase}¡¡¡---")
            clase_reclutada = clase_metodos[clase_personaje].clase
            print("\t\tTus estadisticas de inicio son: \n")
            self.guardar_jugador(clase_reclutada)
            self.mostrar_jugador(self.id_player)
            print(
                f"Ataque: {clase_metodos[clase_personaje].ataque} \t Defensa: {clase_metodos[clase_personaje].defensa}"
                f"\t\t Magia: {clase_metodos[clase_personaje].magia}")
            print(f"HP: {clase_metodos[clase_personaje].hp} \t\t MP: {clase_metodos[clase_personaje].mp} "
                  f"\t\t\t Resistencia: {clase_metodos[clase_personaje].resistencia}")
            print(
                f"Suerte: {clase_metodos[clase_personaje].suerte} \t Inteligencia: {clase_metodos[clase_personaje].inteligencia}"
                f"\tCarisma: {clase_metodos[clase_personaje].carisma}")
        contador_jugadores += 1

    def guardar_jugador(self, cla):
        # El id toma el valor posicional para acceder a los datos
        jugadores[self.id_player] = {
            "nombre": self.nombre,
            "nickname": self.nickname,
            "clase": cla,
            "nivel": self.nivel,
            "experiencia": self.experiencia,
            "equipo_arma": self.equipo_arma,
            "equipo_armadura": self.equipo_armadura,
        }

        return self.id_player

    def mostrar_jugador(self, id_):
        # retorno = clase_metodos[clase_personaje]()
        if id_ in jugadores:
            jugador = jugadores[id_]
            print(f"Nombre: {jugador['nombre']}")
            print(f"Nickname: {jugador['nickname']}")
            print(f"Clase: {jugador['clase']}")
            print(f"Nivel: {jugador['nivel']}")
            print(f"Experiencia: {jugador['experiencia']}")
            print("\n")
            """print(f"Equipo de Armas: {jugador['equipo_arma']}")
            print(f"Equipo de Armadura: {jugador['equipo_armadura']}")
            print(f"Mochila: {jugador['mochila']}")"""
        else:
            print("Jugador no encontrado.")



