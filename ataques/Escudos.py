class Escudos:
    def __init__(self, defensa, descripcion, cod_escudo):
        self.defensa = defensa
        self.descripcion = descripcion
        self.cod_escudo = cod_escudo


class Sh_Mad(Escudos):
    def __init__(self, defensa, descripcion, cod_escudo):
        super().__init__(
            defensa=5,
            descripcion="Escudo de madera para principiantes, no provee de mucha proteccion",
            cod_escudo="SH_MAD"
        )


class Sh_Hrr(Escudos):
    def __init__(self, defensa, descripcion, cod_escudo):
        super().__init__(
            defensa=10,
            descripcion="Escudo de madera para principiantes, no provee de mucha proteccion",
            cod_escudo="SH_HRR"
        )


class Sh_Ace(Escudos):
    def __init__(self, defensa, descripcion, cod_escudo):
        super().__init__(
            defensa=15,
            descripcion="Escudo de madera para principiantes, no provee de mucha proteccion",
            cod_escudo="SH_ACE"
        )