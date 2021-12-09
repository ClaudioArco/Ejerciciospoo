class Electrodomestico:

    def __init__(self, precioBase=100, color="blanco", consumoEnerguia='F', peso=5):
        if color in ("blanco", "negro", "gris", "rojo", "azul"):
            self.color = color
        self.precioBase = precioBase
        self.comprobarConsumoEnergetico(consumoEnerguia)
        self.peso = peso

    def comprobarConsumoEnergetico(self, consumoEnerguia):
        upper_consumEnerguia = consumoEnerguia.upper()
        if upper_consumEnerguia in ("A", "B", "C", "D", "E", "F"):
            self.consumoEnerguia = consumoEnerguia

    def precioFinal(self):
        if self.consumoEnerguia == 'A':
            self.precioBase = self.precioBase + 100
        elif self.consumoEnerguia == 'B':
            self.precioBase = self.precioBase + 80
        elif self.consumoEnerguia == 'C':
            self.precioBase = self.precioBase + 60
        elif self.consumoEnerguia == 'D':
            self.precioBase = self.precioBase + 50
        elif self.consumoEnerguia == 'E':
            self.precioBase = self.precioBase + 30
        elif self.consumoEnerguia == 'F':
            self.precioBase = self.precioBase + 10

        if 0 < self.peso < 20:
            self.precioBase = self.precioBase + 10
        elif 20 < self.peso < 49:
            self.precioBase = self.precioBase + 50
        elif 50 < self.peso < 79:
            self.precioBase = self.precioBase + 80
        elif self.peso < 80:
            self.precioBase = self.precioBase + 100
