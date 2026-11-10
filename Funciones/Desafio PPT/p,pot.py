for i in range(3):
        print("-1. Piedra /n -2. Papel /n-3. Tijera")
        jugador = int(input("Eliga una opcion"))
        print("-1. Piedra /n -2. Papel /n-3. Tijera")
        maquina = int(input("Eliga una opcion"))

def verificar_ganador(jugador, maquina):
        if jugador == 1:
                if maquina == 1:
                        resultado = "Empate"
                elif maquina == 2:
                        resultado = "Gana "