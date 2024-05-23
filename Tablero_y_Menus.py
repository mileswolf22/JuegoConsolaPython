import random

import numpy as np

from VJ_TRY.ataques.Batallas import Batalla_individual

batallas = Batalla_individual


def accion_derivada_de_dados(func):
    def calcular_resultado(*args, **kwargs):
        # Se utiliza args y kwargs para preparar al decorador
        # y almacenar el valor de retorno de lanzar_dado
        resultado = func(*args, **kwargs)
        resultado2 = func(*args, **kwargs)
        if resultado == resultado2:
            sumatoria_par = resultado + resultado2
            return True, sumatoria_par

        else:
            sumatoria_impar = resultado + resultado2
            return False, sumatoria_impar

    return calcular_resultado()


# Pruebas de rellenado de elementos aleatorios en tablero
elementos_mapa = [
    "[Po]",  # Pocion
    "[Ar]",  # Arma
    "[En]",  # Enememigo
    "[Es]",  # Escudo
    "[FM]",  # Fuente Magica
    "[Cm]"  # Campamento
]

# Establecer contadores para indicar cuantas iteraciones se llevaran acabo
elementos_contadores = [
    10,  # Pocion
    5,  # Arma
    20,  # Enemigo
    5,  # Escudo
    2,  # Fuente Magica
    5  # Campamento
]

matriz_tablero = np.array([["[  ]" for _ in range(10)] for _ in range(10)])
"""matriz_tablero = np.array([
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
])"""


class Menus:
    def __init__(self):
        pass

    @staticmethod
    @accion_derivada_de_dados
    def lanzar_dado():
        # Debido al decorador, esta funcion retornara una tupla
        # que contendra tanto un booleano como la sumatoria

        # Se lanza el dado dos veces
        dado = [1, 2, 3, 4, 5, 6]
        resultado = random.choice(dado)
        return int(resultado)

    @staticmethod
    @accion_derivada_de_dados
    def lanzar_dado2():
        # Debido al decorador, esta funcion retornara una tupla
        # que contendra tanto un booleano como la sumatoria

        # Se lanza el dado dos veces
        dado = [1, 2, 3, 4, 5, 6]
        resultado = random.choice(dado)
        return int(resultado)

    @staticmethod
    def crear_mapa(matriz):

        # Indice_ele_lista toma el tamaño de element, el cual es una lista de elementos
        # En este caso, indice_ele_lista = 6
        for indice_ele_lista in range(len(elementos_mapa)):
            # elemento y contador tomar los valores que se encunetren en element y counter
            elemento = elementos_mapa[indice_ele_lista]
            contador = elementos_contadores[indice_ele_lista]

            # El contenido de elemento se imprime las veces que contador indique
            while contador > 0:
                rand_x = random.randint(0, 9)
                rand_y = random.randint(0, 9)
                if matriz[rand_x][rand_y] == "[  ]":
                    matriz[rand_x][rand_y] = elemento
                    contador -= 1

        # El ciclo se repite segun la cantidad del tamaño  en indice_ele_lista
        return matriz

    @staticmethod
    def ver_mapa(matriz_tablero_):
        for fila in matriz_tablero_:
            print(" ".join(fila))

    def menu_batalla(self, vida_protagonista, vida_enemigo, nombre_protagonista, clase_protagonista, clase_enemigo):

        acciones = {
            1: "Atacar",
            2: "Defender",
            3: "Magia",
            4: "Dialogar",
            5: "Items",
            6: "Huir"
        }

        print("\t-------¡¡¡Comienza la batalla!!!----------")
        print(f"\tSe enfrentan {nombre_protagonista} el {clase_protagonista} vs {clase_enemigo}")
        print("\n")
        print("Los combatientes lanzan los dados")

        # Obtengo dos valores: un booleando que da True en caso de ser numeros par y un False en caso de impar
        # El segundo valor es la sumatoria de ambos dados lanzados
        # Quien obtenga un numero mayor comienza el combate
        # Quien obtenga numeros par (True) tendra una bonificacion del 25% de ataque y 25% de defensa

        lanzar_dado_aliado = self.lanzar_dado
        lanzar_dado_enemigo = self.lanzar_dado2

        print(f"Resultado aliado: {lanzar_dado_aliado[1]} \t vs \t Resultado enemigo: {lanzar_dado_enemigo[1]}")
        print("\n")

        if lanzar_dado_aliado[1] > lanzar_dado_enemigo[1]:
            print("Comienzas tu!!!")

            print(f"1.{acciones.get(1)} \t 2.{acciones.get(2)} \t 3.{acciones.get(3)} \n 4.{acciones.get(4)}"
                  f"\t 5.{acciones.get(5)} \t 6.{acciones.get(6)}")

            accion = input("Accion: ")
            resultado = acciones.get(int(accion))
            if accion in acciones:

                if resultado == 1:
                    pass
                elif resultado == 2:
                    pass
                elif resultado == 3:
                    pass
                elif resultado == 4:
                    pass
                elif resultado == 5:
                    pass
                elif resultado == 6:
                    pass

        else:
            print(f"Comienza {clase_enemigo}")
