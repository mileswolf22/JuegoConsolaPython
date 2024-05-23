from VJ_TRY.Tablero_y_Menus import Menus

escenario = Menus()


class Acciones:

    def avanzar_tablero(self, posicion_actual, movimiento, dado):
        i, j = posicion_actual
        if movimiento == 'W':
            i = max(i - dado, 0)  # Arriba
        elif movimiento == 'A':
            j = max(j - dado, 0)  # Izquierda
        elif movimiento == 'S':
            i = min(i + dado, 99)  # Abajo
        elif movimiento == 'D':
            j = min(j + dado, 99)  # Derecha
        return i, j
