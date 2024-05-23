from VJ_TRY.ataques.Armas import *
from Personaje import *


class Enemigo:

    def __init__(self, hp, mp, ataque, defensa, defensa_magica, magia, resistencia, clase, exp):
        self.hp = hp
        self.mp = mp
        self.ataque = ataque
        self.defensa = defensa
        self.defensa_magica = defensa_magica
        self.defensa_magia = defensa_magica
        # Magia cuenta como ataque magico
        self.magia = magia
        self.resistencia = resistencia
        self.clase = clase
        self.exp = exp


class Duende(Enemigo):
    duende = Enemigo

    def __init__(self):
        super().__init__(hp=40, mp=0, ataque=50, defensa=25, defensa_magica=30, magia=0, resistencia=15, exp=20,
                         clase="Duende")


class Duende_Oscuro(Enemigo):
    def __init__(self):
        super().__init__(hp=60, mp=0, ataque=18, defensa=10, defensa_magica=40, magia=0, resistencia=18, exp=35,
                         clase="DuendeOscuro")


class Ogro(Enemigo):
    def __init__(self):
        super().__init__(hp=200, mp=0, ataque=75, defensa=85, defensa_magica=60, magia=0, resistencia=25, exp=45,
                         clase="Ogro")


class Orco(Enemigo):
    def __init__(self):
        super().__init__(hp=120, mp=0, ataque=45, defensa=125, defensa_magica=90, magia=0, resistencia=20, exp=70,
                         clase="Orco")
