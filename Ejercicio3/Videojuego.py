class Videojuego:
    def __init__(self, titulo="", horasEstimadas=10, entregado=False, genero="", comp=""):
        self.titulo = titulo
        self.horasEstimadas = horasEstimadas
        self.entregado = entregado
        self.genero = genero
        self.comp = comp

    def __str__(self):
        return str(self.titulo + ", " + repr(self.horasEstimadas) + ", " +  repr(self.entregado) + ", " + self.genero + ", " + self.comp)