class Armas:
    # cod_arma y cod_escudo son variables la forma en la que
    # se identificaran las armas y los escudos dentro de
    # las listas de la mochila, se guardara unicamente
    # su nomenclatura, cuando se tenga que cargar se iterara
    # sobre la lista para comprobar las nomenclaturas almacenadas

    # To do:
    # Algoritmo que revise si hay mas de una coincidencia dentro
    # del inventario

    def __init__(self, ataque, agilidad, critico, descripcion, cod_arma):
        self.ataque = ataque
        self.agilidad = agilidad
        self.critico = critico
        self.descripcion = descripcion
        self.cod_arma = cod_arma

    # habilidad = ""

    # Nomenclaturas (Armas):
    # ES    - Espada
    # ES_L  - Espada Larga
    # LAN   - Lanza
    # DA    - Daga
    # ARC   - Arco
    # FL    - Flechas
    # GN    - Guantes
    # VAR   - Vara
    # CET   - Cetro
    # SH    - Escudo
    # SH_A  - Escudo de brazo

    # Nomenclaturas (Tipo de):
    # MAD - Madera
    # HRR - Hierro
    # ACE - Acero
    # ACE_CARB


# Espadas Normales
class Es_mad(Armas):
    def __init__(self):
        super().__init__(
            ataque=8,
            agilidad=10,
            critico=.2,
            cod_arma="ES_MAD",
            descripcion="Espada de madera sencilla para principiantes"
        )


class Es_Hrr(Armas):
    def __init__(self):
        super().__init__(
            ataque=10,
            agilidad=12,
            critico=.5,
            cod_arma="ES_HRR",
            descripcion="Espada de hierro convencional, diseñada para aprendices intermedios"
        )


class Es_Ace(Armas):
    def __init__(self):
        super().__init__(
            ataque=18,
            agilidad=10,
            critico=.10,
            cod_arma="ES_ACE",
            descripcion="Espada de acero, su filo y potencia son claramente apreciables"
        )


# Espadas Largas
class Es_L_Mad(Armas):
    def __init__(self):
        super().__init__(
            ataque=10,
            agilidad=6,
            critico=.8,
            cod_arma="ES_L_MAD",
            descripcion="Espada larga de madera, util para entrenamientos primerizos"
        )


class Es_L_Hrr(Armas):
    def __init__(self):
        super().__init__(
            ataque=15,
            agilidad=4.5,
            critico=.10,
            cod_arma="ES_L_MAD",
            descripcion="Espada larga de hierro, tiene un peso considerable para golpes contundentes"
        )


class Es_L_Ace(Armas):
    def __init__(self):
        super().__init__(
            ataque=15,
            agilidad=4.5,
            critico=.10,
            cod_arma="ES_L_ACE",
            descripcion="Espada larga de acero, ideal para usuario avanzados, su filo es bastante fino y peligroso"
        )


