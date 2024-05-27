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

    @staticmethod
    def verificar_casilla(casilla_cont):

        casilla = casilla_cont
        if casilla == "[Po]":
            print("Encontraste Pocion")
        elif casilla == "[Ar]":
            print("Encontraste Arma")
        elif casilla == "[En]":
            print("Encontraste Enemigo")
        elif casilla == "[Es]":
            print("Encontraste Escudo")
        elif casilla == "[Fm]":
            print("Encontraste Fuente Magica")
        elif casilla == "[Cm]":
            print("Encontraste Campamento")
        elif casilla == "[  ]":
            print("Vacio")

    # Primer movimiento
    def avanzar_tablero(self, matriz, posicion_anterior, posicion_actual, movimiento, dado, contenido_anterior):
        # Obtener las posiciones anteriores y actuales
        ant_pos = posicion_anterior
        new_pos = posicion_actual
        pos_contenido_anterior = contenido_anterior
        print(f"Dado: {dado}")
        print(f"Posicion anterior: {ant_pos}")
        print(f"Contenido Pos Anterior: {pos_contenido_anterior}")
        # Encontrar la posición actual del jugador en la matriz
        pos = np.where(matriz == new_pos)
        posiciones = list(zip(pos[0], pos[1]))
        print(f"pos: {pos}")
        print(f"Posiciones: {posiciones}")
        posiciones_jugador = list(posiciones)
        print(posiciones_jugador)
        # Si hay múltiples posiciones, seleccionamos la primera
        if len(posiciones) > 0:
            i, j = posiciones[0]
        else:
            raise ValueError("No se encontró la posición actual en la matriz")

        # Calcular la nueva posición basada en el movimiento y el dado
        if movimiento == 'W':  # Arriba
            i = max(i - dado, 0)
            print(f"Movimiento a: {i}, {j}")
        elif movimiento == 'A':  # Izquierda
            j = max(j - dado, 0)
            print(f"Movimiento a: {i}, {j}")
        elif movimiento == 'S':  # Abajo
            i = min(i + dado, len(matriz) - 1)
            print(f"Movimiento a: {i}, {j}")
        elif movimiento == 'D':  # Derecha
            j = min(j + dado, len(matriz[0]) - 1)
            print(f"Movimiento a: {i}, {j}")
        else:
            raise ValueError("Movimiento no válido. Use 'W', 'A', 'S' o 'D'.")

        # Actualizar la matriz
        elemento_antes_pos_jg = matriz[i, j]
        matriz[ant_pos[0], ant_pos[1]] = "[  ]"  # Asumimos que "[  ]" es el estado vacío
        matriz[i, j] = new_pos

        print(f"Antes de JG: {elemento_antes_pos_jg}")

        return [i, j], elemento_antes_pos_jg

        # Codigo Anterior

        # ant_pos = posicion_anterior  # Mi intencion es conocer que habia antes del cambio del jugador
        # new_pos = posicion_actual  # Nueva marca del jugador
        # No tome en consideracion que los elementos dentro del mapa
        # se repiten varias veces, causando que
        # print(ant_pos)
        # print(new_pos)
        # print(matriz)
        # pos = np.where(matriz == new_pos)
        # print(f"pos: {pos}")
        # posiciones = list(zip(pos[0], pos[1]))
        # print(f"posiciones: {posiciones[0][1]}")
        # if movimiento == 'W':
        # i = max(posiciones[0] - dado, 0)  # Arriba
        # elif movimiento == 'A':
        # j = max(posiciones[1] - dado, 0)  # Izquierda
        # elif movimiento == 'S':
        # i = min(posiciones[0] + dado, 9)  # Abajo
        # elif movimiento == 'D':
        # j = min(posiciones[1] + dado, 9)  # Derecha
        # return [i, j]

    @staticmethod
    def actualizar_movimiento(posicion_anterior, dado):
        pass
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

