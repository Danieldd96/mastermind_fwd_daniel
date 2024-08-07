from player import Creador, Adivinador,CPU
from tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero()

    def bienvenida(self):
        print("Bienvenido a Mastermind")
        print("---------------------")
        opcion = input("Elige como quieres jugar: como creador del código (c) o como adivinador (g)? ").strip().upper()
        
        if opcion == "C":
            self.creador = Creador()
            self.creador.set_combinacion()
            self.adivinador = CPU(self.creador.combinacion)  # La CPU adivinará el código
        elif opcion == "G":
            self.adivinador = Adivinador()
            self.creador = Creador()
            self.creador.codigo_random()
        else:
            print("Opción no reconocida. Saliendo del juego.")
            return
        
        self.iniciar_juego()

    def iniciar_juego(self):
        for i in range(12):
            adivinanza = self.adivinador.hacer_adivinanza()
            retroalimentacion = self.creador.get_retroalimentacion(adivinanza)
            self.tablero.actualizar_tablero(adivinanza, retroalimentacion)
            self.tablero.mostrar_tablero()
            
            if retroalimentacion.count("verde") == 4:
                print("¡Felicidades! Has adivinado la combinación.")
                return
        
        print("Se acabaron los intentos. El código a adivinar era:", self.creador.combinacion)


juego = Juego()
juego.bienvenida()
