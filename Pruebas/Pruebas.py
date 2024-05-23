import numpy as np
from  VJ_TRY.Tablero_y_Menus import Menus
from VJ_TRY.Clases_y_Personajes.Mochila import Mochila
# Pruebas para implementar en el codigo principal
import random

from VJ_TRY.Clases_y_Personajes.Acciones import Acciones

# Pruebas de combate (funciona)
"""from VJ_TRY.Clases import Guerrero
from VJ_TRY.Enemigo import Duende
from VJ_TRY.ataques.Armas import Es_mad

war = Guerrero()
duende = Duende()
arma = Es_mad()


def batalla(jugador_clase, jugador_hp, jugador_defensa, jugador_resistencia,
            enemigo_clase, enemigo_hp, enemigo_defensa, enemigo_resistencia):
    print("Comienza la batalla")
    print(f"El {jugador_clase} cuenta con {jugador_hp} punto de vida")
    print(f"El {enemigo_clase} cuenta con {enemigo_hp} punto de vida")
    print("\n")

    total_dano_jugador_e = war.ataque_fisico(arma.ataque, enemigo_defensa, enemigo_resistencia)
    print(f"{jugador_clase} inflinge {total_dano_jugador_e} de daño a {enemigo_clase}!!")
    resta_vida = enemigo_hp - total_dano_jugador_e
    vida_jugador = round(resta_vida)
    print(f"A {enemigo_clase} le restan {resta_vida}")

    print("\n")
    total_dano_enemigo_j = duende.ataque_fisico(arma.ataque, jugador_defensa, jugador_resistencia)
    print(f"{enemigo_clase} inflinge {total_dano_enemigo_j} de daño a {jugador_clase}!!")
    resta_vida_enemigo = vida_jugador - total_dano_enemigo_j
    vida_enemigo = round(resta_vida_enemigo)
    print(f"A {jugador_clase} le restan {resta_vida_enemigo}")

    return vida_jugador, vida_enemigo


print("\n")
valores = batalla(war.clase, war.hp, war.defensa, war.resistencia,
                  duende.clase, duende.hp, duende.defensa, duende.resistencia)

vida_jugador = valores[0]
vida_enemigo = valores[1]

if vida_jugador >= 0 or vida_enemigo != 0:
    print("Entra if")
    batalla(war.clase, vida_jugador, war.defensa, war.resistencia,
            duende.clase, vida_enemigo, duende.defensa, duende.resistencia)

    if vida_jugador <= 0 or vida_enemigo <= 0:
        print("Batalla terminada")
    else:
        pass"""

"""actor = Personaje()
enemigo = Enemigo
arma = Armas()

enemigo_duende = Duende()
vida_e = enemigo_duende.hp
ataque_e = enemigo_duende.ataque
defensa_e = enemigo_duende.defensa
resistencia = enemigo_duende.resistencia
clase = actor.guerrero()


def golpe_actor():
    calcular_ataque_jugador = enemigo_duende.defensa / actor.ataque
    calcular_resistencia = enemigo_duende.resistencia / calcular_ataque_jugador
    total_ataque = calcular_ataque_jugador - calcular_resistencia
    vida_restante = enemigo_duende.hp - total_ataque

    enemigo_duende.hp = vida_restante
    return vida_restante



while enemigo_duende.hp != 0:
    golpe_vidarestante = golpe_actor()
    print(golpe_vidarestante)
"""
"""from VJ_TRY.Clases_y_Personajes.Acciones import *

action = Acciones()

action.menu_batalla("Delta", "Mago Blanco", "Duende")"""

# Pruebas de tablero (funciona)
"""from VJ_TRY.Clases_y_Personajes.Acciones import Acciones
from VJ_TRY.Tablero_y_Menus import Menus
from VJ_TRY import Tablero_y_Menus
import numpy as np

menu = Menus()
table = Tablero_y_Menus
accion = Acciones()

matriz = menu.crear_tablero()  # Matriz del tablero
dado_lanzado = menu.lanzar_dado
aleatorio_x = random.randint(0, 9)
aleatorio_y = random.randint(0, 9)

posicion_inicial = (0, 0)  # Tupla inmutable
posicion_anterior = [0, 0]  # Lista mutable
posicion_siguiente = [0, 1]
posicion_jugador = posicion_inicial

print(f"Posicion del jugador: {posicion_inicial}")


def mover(matriz_, posicion, dado, movimiento):
    x, y = posicion  # Desempaquetamos la posicion inicial

    filas, columnas = matriz_.shape  # Obtenemos el tamaño  de la matriz

    if movimiento in ('W', 'A', 'S', 'D'):
        if movimiento == 'W':
            print("Movimineto en W")
            x = max(x - dado, 0)
        elif movimiento == 'A':
            print("Movimineto en A")
            y = max(y - dado, 0)
        elif movimiento == 'S':
            print("Movimineto en S")
            x = min(x + dado, filas - 1)
        elif movimiento == 'D':
            print("Movimineto en D")
            y = min(y + dado, columnas - 1)

    return x, y


resultado_x, resultado_y = mover(matriz, posicion_inicial, 30, 'S')
print(f"x: {resultado_x}, y: {resultado_y}")
posicion_anterior[0] = posicion_siguiente[0]
posicion_anterior[1] = posicion_siguiente[1]

posicion_siguiente[0] += resultado_x  # Se actualiza la posicion sumando la anterior
posicion_siguiente[1] += resultado_y  # por la nueva
print(f"Posicion anterior del jugador: {posicion_anterior[0], posicion_anterior[1]}")
print(f"Nueva posicion del jugador: {posicion_siguiente[0], posicion_siguiente[1]}")"""

# Funciona, ahora falta implementarlo dentro del juego principal
# Aunque la funcionalidad base de movimiento ya esta alli


# Pruebas de rellenado de elementos aleatorios en tablero
"""elementos_mapa = [
    "[Po]",  # Pocion
    "[Ar]",  # Arma
    "[En]",  # Enememigo
    "[Es]",  # Escudo
    "[FM]",  # Fuente Magica
    "[Cm]"   # Campamento
]

# Establecer contadores para indicar cuantas iteraciones se llevaran acabo
elementos_contadores = [
    10,  # Pocion
    5,   # Arma
    20,  # Enemigo
    5,   # Escudo
    2,   # Fuente Magica
    5    # Campamento
]

# Tablero de string
# Segun el valor de la casilla se activara un evento
matriz_tablero = np.array([["[  ]" for _ in range(10)] for _ in range(10)])



# crear una serie de iteraciones randoms en xy para asignar los elementos
def crear_mapa(matriz, element, counter):
    # Indice_ele_lista toma el tamaño de element, el cual es una lista de elementos
    # En este caso, indice_ele_lista = 6
    for indice_ele_lista in range(len(element)):

        # elemento y contador tomar los valores que se encunetren en element y counter
        elemento = element[indice_ele_lista]
        contador = counter[indice_ele_lista]

        # El contenido de elemento se imprime las veces que contador indique
        while contador > 0:
            rand_x = random.randint(0, 9)
            rand_y = random.randint(0, 9)
            if matriz[rand_x][rand_y] == "[  ]":
                matriz[rand_x][rand_y] = elemento
                contador -= 1

    # El ciclo se repite segun la cantidad del tamaño  en indice_ele_lista
    return matriz


matrix = crear_mapa(matriz_tablero, elementos_mapa, elementos_contadores)

for fila in matriz_tablero:
    print(" ".join(fila))


def verificar_casilla(matrix_):
    posicion_jugador_x = random.randint(1, 9)
    posicion_jugador_y = random.randint(1, 9)

    casilla = matrix_[posicion_jugador_x][posicion_jugador_y]
    if   casilla == "[Po]":
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


print("\n")
verificar_casilla(matrix)"""

# Crear una mochila funcional (Funciona)
"""mochila = Mochila
mochi = mochila.crear_mochila(1234)"""


# mochi[1234]["Equipables"]["Armas"]["Espadas"].append("Espada de Madera")
# inventario = mochi[1234]["Equipables"]["Armas"]["Espadas"]

# print(f"Espadas: {inventario}")

"""def visaulizar_inventario(id_user):
    global armas_disponibles
    print("----------------Mochila--------------------")
    print("1. Armas \t 2. Armaduras")
    print("3. Consumibles \t 4. Objetos")

    seccion = int(input("Seccion: "))
    print("\n")
    if seccion == 1:
        print("-------Armas-------")
         
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


visaulizar_inventario(1234)"""

menu = Menus
matriz_tablero = np.array([["[  ]" for _ in range(10)] for _ in range(10)])
tablero = menu.crear_mapa(matriz_tablero)

for fila in tablero:
    print(" ".join(fila))
rand_x = random.randint(1,9)
rand_y = random.randint(1, 9)

jugador = tablero[rand_x][rand_y]

if jugador == "[En]":
    print("Te has encontrado con un enemigo")
else:
    print("Te salvaste")

