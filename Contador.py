class Contador:
    # Variable de clase, accesible solo dentro de la clase
    __contador_general = 0

    def __init__(self):
        # Incrementar el contador general cada vez que se crea una instancia
        Contador.__contador_general += 1
        # Variable de instancia
        self.__mi_contador = 0

    def incrementar(self):
        self.__mi_contador += 1

    def valor(self):
        return self.__mi_contador

    @classmethod
    def valor_general(cls):
        return cls.__contador_general

# Crear instancias de la clase Contador
c1 = Contador()
c2 = Contador()

# Incrementar el contador de c1 y c2
c1.incrementar()
c1.incrementar()
c2.incrementar()

print("Valor del contador c1:", c1.valor())  # Salida: 2
print("Valor del contador c2:", c2.valor())  # Salida: 1
print("Valor del contador general:", Contador.valor_general())  # Salida: 2
