class Serie:
    def __init__(self,titulo="", numTemp=3, entregado=False, genero="", creador=""):
        self.titulo = titulo
        self.numTemp = numTemp
        self.entregado = entregado
        self.genero = genero
        self.creador = creador

    def __str__(self):
        return str(self.titulo + ", " + repr(self.numTemp) + ", " + repr(self.entregado) + ", " + self.genero + ", " + self.creador)