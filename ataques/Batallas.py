# De aqui beberan tanto el prota como los enemigos en el caso de los combates individuales
# Tener en cuenta de no confundir los parametros protagonista y enemigo

# Cuando el heroe es quien ataca toma los parametros protagonista y el enemigo los de enemigo
# Cuando el enemigo es quien ataca toma los parametros protagonista y el heroe los del enemigo

class Batalla_individual:
    def __init__(self, protagonista, enemigo):
        self.protagonista = protagonista
        self.enemigo = enemigo

    # Referente a Heroe
    @staticmethod
    # Veirificar bien todos los metodos por que los copie de los enemigos
    def ataque_fisico(arma, ataque_prota, defensa_enemigo, resistencia_enemigo):
        cal_dano_heroe = ((ataque_prota + arma) / defensa_enemigo) * 10
        valorar_resistencia = cal_dano_heroe / resistencia_enemigo
        dano_total = round(cal_dano_heroe - valorar_resistencia)

        return dano_total

    @staticmethod
    # Recibe como parametro el valor de defensa magica(DM) del enemigo (Aunque no todos tienen DM)
    # Valor_hechizo es la cantidad de poder magico que posee un hechizo en particular
    def ataque_hechizo(magia_prota, valor_hechizo, defensa_magica_enemigo, resistencia_enemigo):
        cal_dano_heroe = ((magia_prota + valor_hechizo) / defensa_magica_enemigo) * 10
        # La resistencia natural tambien entra en juego en el ataque magico
        valorar_resistencia = cal_dano_heroe / resistencia_enemigo
        dano_realizado = round(cal_dano_heroe - valorar_resistencia, 2)

        # Se devuelve el daño realizado
        # Sera necesario restar este valor de la vida del enemigo
        return dano_realizado

    @staticmethod
    def defensa_fisica(ataque_enemigo, defensa_prota, resistencia_prota):
        # cal_defensa realiza el calculo del ataque dividida por la defensa del jugador
        cal_defensa = ataque_enemigo / defensa_prota
        # Se valora la resistencia en funcion del ataque del enemigo
        implementar_resistencia = ataque_enemigo / resistencia_prota
        # Se redonde la suma de la defensa realizada + la resistencia calculada
        dano_defendido = round(cal_defensa + implementar_resistencia)

        # Se devuelve el daño defendido
        # Sera necesario restar este valor de la vida del jugador
        return dano_defendido

    # Este metodo se usara unicamente cuando el ataque sea magico
    @staticmethod
    def defensa_magica_(defensa_magica_prota, resistencia_prota, magia_enemigo, valor_hechizo):
        # cal_defensa realiza el calculo del ataque dividida por la defensa del jugador
        cal_defensa = (magia_enemigo + valor_hechizo) / defensa_magica_prota
        # Se valora la resistencia en funcion del ataque del enemigo
        implementar_resistencia = magia_enemigo / resistencia_prota
        # Se redonde la suma de la defensa realizada + la resistencia calculada
        dano_defendido = round(cal_defensa + implementar_resistencia)

        # Se devuelve el daño defendido
        # Sera necesario restar este valor de la vida del jugador
        return dano_defendido




class BatallaDoble:
    def __init__(self, protagonista, enemigo, enemigo2):
        self.protagonista = protagonista
        self.enemigo = enemigo
        self.enemigo2 = enemigo2

    # Pendiente
