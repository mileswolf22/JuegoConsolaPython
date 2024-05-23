# Pruebas random que no se implementaran
import numpy as np

# Crear un diccionario de matrices

dic_matrices = {}
contador = 0

def crear_matriz(filas, columnas):
    global contador
    # CONVERSION A TIPO INT32 DE NUMPY
    fila_ = np.int32(filas)
    columna_ = np.int32(columnas)

    fila = np.arange(fila_, columna_)
    tablero = np.tile(fila, (1, 1))
    contador += 1
    dic_matrices[contador] = tablero
    return tablero, dic_matrices


matrix = crear_matriz(1, 100)
matrix1 = crear_matriz(1, 1)

print(f'Tablero: {matrix[0]}')
print("\n\n\n")
print(f'Matriz: {matrix[1]}')

print("\n\n\n")
mi_matriz = dic_matrices[1]
mi_matriz[0][2] = 250

print(mi_matriz)

# Matriz de strings
matriz_string = np.array([
    ["Pos0.0", "Pos1.0", "Pos2.0", "Pos3.0", "Pos4.0", "Pos5.0", "Pos6.0", "Pos7.0", "Pos.08", "Pos9.0"],
    ["Pos0.1", "Pos1.1", "Pos2.1", "Pos3.1", "Pos4.1", "Pos5.1", "Pos6.1", "Pos7.1", "Pos8.1", "Pos9.1"],
    ["Pos0.2", "Pos1.2", "Pos2.2", "Pos3.2", "Pos4.2", "Pos5.2", "Pos6.2", "Pos7.2", "Pos8.2", "Pos9.2"]
])
print("\n\n\n")
print("\n\n\n")
matriz_string[0][2] = "Delta"
print(f"String: {matriz_string}")


# Matriz de funciones (????)

def funcion1(nombre):
    return f"Esta es la funcion {nombre}"


def funcion1_1(nombre):
    print(f"Esta es la funcion {nombre}")


def funcion2():
    print("Esta es la funcion 2")


def funcion3():
    print("Esta es la funcion 3")


matriz_funciones = [
    [funcion1],
    [funcion2],
    [funcion3]
]


def super_deco_matriz(func):
    def recodeco(*args, **kwargs):
        print("Aqui decoramos")
        resultado = func(*args, **kwargs)
        print(resultado)
        print("Y luego nos vamos")
        return resultado

    return recodeco


# Evitar poner el parentesis en la funcion decorada
# esto es para que no se llame la funcion decorada
# sino que cimplemente se devuelva

@super_deco_matriz
def decorar_matriz(nombre):
    var = matriz_funciones[0][0](nombre)
    return var


delta = decorar_matriz("Pepe")
