#Funcion Potencia y raiz cuadrada

leerNumeros = lambda: (int(input("Dame el primer numero: ")), int(input("Dame el segundo numero: ")))

class Potencia:
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcularPotencia(self):
        return self.base ** self.exponente
    
class RaizCuadrada:
    def calcularRaiz(self):
        return self.numero ** 0.5    
    

    

    
