from colored import fg,attr
class Tablero:
    COLORES = {
        'red': fg("red"),
        'blue': fg("blue"),
        'yellow': fg("yellow"),
        'green': fg("green")
    }
    
    def __init__(self):
        self.__combinacion = []
        self.__turnos = []
        
    def creacion_color(self, color):
        self.__combinacion = color
        
    def validar(self, intento):
        retroalimentacion = []
        colores_copia = self.__combinacion.copy()
        for i in range(4):
            if intento[i] == colores_copia[i]:
                retroalimentacion.append("verde")
                colores_copia[i] = None
            elif intento[i] in colores_copia:
                retroalimentacion.append("amarillo")
                colores_copia.remove(intento[i])
            else:
                retroalimentacion.append("blanco")
        
        return retroalimentacion

    def mostrar_tablero(self):
        for intento, retroalimentacion in self.__turnos:
            fila = ' '.join([self.COLORES[color] + "O" + attr("reset") for color in intento])
            mostrar_retroalimentacion = ' '.join([fg("green") + "o" + attr("reset") if f == "verde"
            else fg("yellow") + "o" + attr("reset") if f == "amarillo"
            else "o"
            for f in retroalimentacion])
            print(f"{fila} | {mostrar_retroalimentacion}")
            
    def actualizar_tablero(self, intento, retroalimentacion):
        self.__turnos.append((intento, retroalimentacion))