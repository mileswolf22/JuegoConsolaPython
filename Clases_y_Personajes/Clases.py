def definicion_de_clase(num):
    int(num)
    if num == 1:
        print("Un imponente guerrero que ha recorrido incontables campos de batalla.\n Su cuerpo está "
              "marcado por cicatrices de antiguos combates, testigos de su valentía y tenacidad.\n Porta una "
              "armadura pesada y empuña una gran espada que brilla con la promesa de la victoria.\n Con una mirada "
              "fiera y una sonrisa desafiante,\n el guerrero se enfrenta a cualquier enemigo con determinación y "
              "coraje.\n")
    elif num == 2:
        print("Un mago blanco cuyo corazón rebosa de compasión y luz.\n Su presencia irradia una aura de "
              "calma y esperanza, y sus ojos reflejan la sabiduría de los siglos.\n Ataviado con túnicas blancas "
              "adornadas con símbolos sagrados, lleva consigo un báculo que brilla con la luz curativa.\n "
              "Con cada palabra, canaliza el poder divino para sanar heridas y restaurar la esperanza en los "
              "corazones afligidos.\n Siempre está listo para ofrecer ayuda a aquellos que lo necesitan y luchar "
              "contra las fuerzas oscuras con su fe inquebrantable.")
    elif num == 3:
        print("Mago oscuro cuyo poder está envuelto en sombras y secretos prohibidos. Su mirada "
              "fría y penetrante esconde un conocimiento profundo de las artes arcanas más oscuras. Vestido con "
              "túnicas negras que parecen absorber la luz, emana una presencia ominosa que inspira temor "
              "en aquellos que se cruzan en su camino. Con gestos siniestros, conjura sombras y maldiciones que "
              "corrompen y debilitan a sus enemigos. Siempre en busca de poder y conocimiento, el mago oscuro no dudará"
              "en usar cualquier medio necesario para alcanzar sus objetivos, incluso si eso significa sacrificar "
              "a otros en el proceso.")
    elif num == 4:
        print("Pícaro de carisma arrollador y habilidades clandestinas. Viste ropas oscuras que se "
              "funden con las sombras y siempre lleva consigo una daga afilada. Con movimientos ágiles y gestos "
              "elegantes, se desliza por las ciudades y los bosques como una sombra, siempre en busca de la "
              "próxima aventura o el próximo tesoro. Su ingenio y astucia son sus armas más poderosas.")
    elif num == 5:
        print("Una cazadora nómada, experta en el arte del arco y la flecha. Sus ojos agudos escrutan el "
              "horizonte en busca de presas o peligros, mientras sus manos hábiles manejan su arco con destreza. "
              "Con un susurro y un ligero estiramiento de la cuerda, suelta su flecha, que vuela con "
              "precisión mortal hacia su objetivo. Con cada tiro, demuestra su habilidad como la mejor arquera de "
              "la región.")
    elif num == 6:
        print("Clérigo devoto, marcado por la gracia divina y la compasión por los demás. Su "
              "presencia irradia una aura de calma y protección, y su voz tiene el poder de traer consuelo a los "
              "afligidos. Con gestos reverentes, canaliza el poder divino para sanar heridas y expulsar la "
              "oscuridad. Siempre está listo para enfrentarse al mal y proteger a los inocentes con su fe "
              "inquebrantable.")
    elif num == 7:
        print("Un paladín cuyo deber es defender la justicia y proteger a los indefensos. Su "
              "armadura resplandece con la luz del sol y su espada está grabada con runas sagradas que brillan "
              "con el poder divino. Con una mirada firme y una postura erguida, emana una presencia "
              "imponente que infunde valor en sus aliados y temor en sus enemigos. Guiado por un código de honor "
              "inquebrantable, el paladin lucha contra la oscuridad con determinación y coraje. Siempre dispuesto "
              "a sacrificarse por el bien mayor, Sir Aldric es el símbolo viviente de la virtud y la justicia en "
              "un mundo lleno de peligros y corrupción.")
    elif num == 8:
        print("Bárbaro colosal, forjado en las heladas estepas del norte. Su cuerpo está cubierto de "
              "tatuajes que cuentan historias de batallas ganadas y enemigos derrotados. Empuña una gran hacha "
              "con una fuerza que parece sacudir la tierra misma. Cuando entra en un frenesí de combate, "
              "su rugido resuena como el trueno, y su furia desata una tormenta de destrucción sobre sus enemigos.")


class Clases:

    def __init__(self,
                 clase,
                 hp,
                 mp,
                 ataque,
                 defensa,
                 defensa_magica,
                 magia,
                 resistencia,
                 suerte,
                 inteligencia,
                 carisma,
                 taza_de_crecimiento_magico,
                 taza_de_aprendizaje
                 ):
        self.clase = clase
        self.hp = hp
        self.mp = mp
        self.ataque = ataque
        self.defensa = defensa
        self.defensa_magica = defensa_magica
        self.magia = magia
        self.resistencia = resistencia
        self.suerte = suerte
        self.inteligencia = inteligencia
        self.carisma = carisma
        self.taza_de_crecimiento_magico = taza_de_crecimiento_magico
        self.taza_de_aprendizaje = taza_de_aprendizaje



class Guerrero(Clases):

    def __init__(self):
        super().__init__(
            clase="Guerrero",
            hp=50,
            mp=15,
            ataque=20,
            defensa=30,
            defensa_magica=20,
            magia=10,
            resistencia=25,
            suerte=18,
            inteligencia=10,
            carisma=5,
            taza_de_crecimiento_magico=.1,
            taza_de_aprendizaje=.1
        )


class Ladron(Clases):

    def __init__(self):
        super().__init__(
            clase="Ladron",
            hp=35,
            mp=20,
            ataque=15,
            defensa=10,
            defensa_magica=15,
            magia=8,
            resistencia=10,
            suerte=30,
            inteligencia=25,
            carisma=30,
            taza_de_crecimiento_magico=.1,
            taza_de_aprendizaje=.1
        )


class Cazador(Clases):
    def __init__(self):
        super().__init__(
            clase="Cazador",
            hp=45,
            mp=15,
            ataque=20,
            defensa=20,
            defensa_magica=15,
            magia=8,
            resistencia=20,
            suerte=20,
            inteligencia=10,
            carisma=10,
            taza_de_crecimiento_magico=.1,
            taza_de_aprendizaje=.1
        )


class Clerigo(Clases):
    def __init__(self):
        super().__init__(
            clase="Clerigo",
            hp=30,
            mp=60,
            ataque=5,
            defensa=10,
            defensa_magica=40,
            magia=35,
            resistencia=10,
            suerte=20,
            inteligencia=35,
            carisma=30,
            taza_de_crecimiento_magico=.5,
            taza_de_aprendizaje=.5
        )


class Paladin(Clases):
    def __init__(self):
        super().__init__(
            clase="Paladin",
            hp=80,
            mp=10,
            ataque=20,
            defensa=40,
            defensa_magica=40,
            magia=10,
            resistencia=35,
            suerte=18,
            inteligencia=10,
            carisma=5,
            taza_de_crecimiento_magico=.1,
            taza_de_aprendizaje=.1
        )


class Barbaro(Clases):
    def __init__(self):
        super().__init__(
            clase="Barbaro",
            hp=50,
            mp=15,
            ataque=20,
            defensa=30,
            defensa_magica=15,
            magia=10,
            resistencia=25,
            suerte=18,
            inteligencia=8,
            carisma=5,
            taza_de_crecimiento_magico=.1,
            taza_de_aprendizaje=.1
        )


class Mago_Blanco(Clases):
    def __init__(self):
        super().__init__(
            clase="MagoBlanco",
            hp=30,
            mp=30,
            ataque=10,
            defensa=30,
            defensa_magica=30,
            magia=38,
            resistencia=25,
            suerte=18,
            inteligencia=20,
            carisma=8,
            taza_de_crecimiento_magico=.10,
            taza_de_aprendizaje=.10
        )


class Mago_Oscuro(Clases):
    def __init__(self):
        super().__init__(
            clase="MagoOscuro",
            hp=35,
            mp=25,
            ataque=25,
            defensa=15,
            defensa_magica=30,
            magia=40,
            resistencia=27,
            suerte=18,
            inteligencia=18,
            carisma=15,
            taza_de_crecimiento_magico=.7,
            taza_de_aprendizaje=.7
        )
