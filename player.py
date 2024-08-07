import random
class Creador:
    def __init__(self) -> None:
        self.combinacion = []
        
    def set_combinacion(self):
        while True:
            codigo = input("Ingresa la combinación entre 4 colores: red, blue, green, yellow: ").strip().lower().split()
            if len(codigo) == 4 and all(color in ["red", "blue", "green", "yellow"] for color in codigo):
                self.combinacion = codigo
                break
            else:
                print("Código no válido. Vuelva a ingresarlo.")
                
    def codigo_random(self):
        self.combinacion = [random.choice(["red", "blue", "green", "yellow"]) for _ in range(4)]
        
    def get_retroalimentacion(self, adivinar):
        retroalimentacion = ["blanco"] * 4
        copia_combinacion = self.combinacion[:]
        copia_adivinar = adivinar[:]

        for i in range(4):
            if copia_adivinar[i] == copia_combinacion[i]:
                retroalimentacion[i] = "verde"
                copia_combinacion[i] = None
                copia_adivinar[i] = "Emparejada"

        for i in range(4):
            if copia_adivinar[i] != "Emparejada" and copia_adivinar[i] in copia_combinacion:
                retroalimentacion[i] = "amarillo"
                copia_combinacion.remove(copia_adivinar[i])
        
        return retroalimentacion
    
class Adivinador:
    def __init__(self) -> None:
        self.adivinar = []
        
    def hacer_adivinanza(self):
        while True:
            codigo_adivinar = input("Haz tu adivinanza: elige entre 4 colores: red, blue, green, yellow: ").strip().lower().split()
            if len(codigo_adivinar) == 4 and all(color in ["red", "blue", "green", "yellow"] for color in codigo_adivinar):
                self.adivinar = codigo_adivinar
                return codigo_adivinar
            else:
                print('Adivinanza no válida. Ingréselo de nuevo.')
class CPU:
    def __init__(self, combinacion_secreta):
        self.combinacion_secreta = combinacion_secreta
        self.intentos = 0

    def generar_adivinanza(self):
        return [random.choice(["red", "blue", "green", "yellow"]) for _ in range(4)]

    def hacer_adivinanza(self):
        self.intentos += 1
        return self.generar_adivinanza()
