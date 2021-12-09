from Electrodomestico import Electrodomestico


class Lavadora(Electrodomestico):
    def __init__(self, precioBase=100, color="blanco", consumoEnerguia='F', peso=5, carga=5):
        Electrodomestico.__init__(self, precioBase=precioBase, color=color, consumoEnerguia=consumoEnerguia, peso=peso)
        self.carga=carga

    def precioFinal(self):
        Electrodomestico.precioFinal(self)
        if self.carga > 30:
            self.precioBase = self.precioBase + 50




