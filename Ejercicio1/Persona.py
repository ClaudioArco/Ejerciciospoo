import random


class Persona:

    def __init__(self):
        self._nombre = ""
        self._dni = 0
        self._edad = 0
        self._sexo = "M"
        self._peso = 0.0
        self._altura = 0.0

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setPeso(self, peso):
        self._peso = peso

    def setSexo(self, sexo):
        self._sexo = sexo

    def setAltura(self, altura):
        self._altura = altura

    def setDNI(self, dni):
        self._dni = dni

    def toString(self, nombre, dni, edad, sexo, peso, altura):
        return nombre + " " + str(dni) + " " + str(edad) + " " + sexo + " " + str(peso) + " " + str(altura)


def introducirSexo():
    sexo = input("Introduce el sexo, H o M, de no ser ninguno de estos, se añadira por defecto M ")
    if sexo != 'H' or sexo != 'M':
        sexo = 'M'
    return sexo


def calcularIMC(peso, altura):
    imc = peso / (altura * 2)
    if 18.5 < imc < 24.9:
        return 0
    elif 25 < imc:
        return 1
    elif imc < 18.5:
        return -1


def esMayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False


def calcularNif(posicionLetras, dni):
    position = dni % 23
    letter = posicionLetras[position]
    return letter


def generarDNI():
    positionsLetters = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q',
                        'V', 'H',
                        'L', 'C', 'K', 'E']

    dni = random.randint(0, 99999999)
    letter = calcularNif(positionsLetters, dni)
    nif = str(dni) + letter
    return nif


p = Persona()
p2 = Persona()
p3 = Persona()
while True:
    altura = float(input("Introduzca su altura "))
    peso = float(input("Introduzca su peso "))

    if 1.00 < altura < 2.10 or 30.0 < peso < 150.0:
        break

p.setPeso = peso
p.setAltura = altura
p3.setPeso = 90.0
p3.setAltura = 1.90

result = calcularIMC(peso, altura)
imc = peso / (altura * 2)
if result == 0:
    print('Peso ideal {:.2f}'.format(imc))
elif result == 1:
    print('Sobrepeso {:.2f}'.format(imc))
elif result == -1:
    print('Peso insuficiente {:.2f}'.format(imc))

while True:
    edad = int(input("Introduzca su edad "))
    if 1 < edad < 100:
        break
p.setEdad = edad
p2.setEdad = edad
p3.setEdad = 25

result2 = esMayorDeEdad(edad)
if result2:
    print("Es mayor de edad")
else:
    print("Todavia no es mayor de edad")

##sexo
sexo = introducirSexo()
p.setSexo = sexo
p2.setSexo = sexo
p3.setSexo = "H"

dni = generarDNI()
p.setDNI = dni
p2.setDNI = dni
p3.setDNI = "78007198F"

nombre = input("Introduzca su nombre ")
p.setNombre = nombre
p2.setNombre = nombre
p3.setNombre = "Javier"

print("Primer objeto: ", p.toString(nombre, dni, edad, sexo, peso, altura))
print("Segundo objeto: ", p2.toString(nombre, dni, edad, sexo, "", ""))
print("Tercer objeto: ", p.toString("claudii", "78113078", 25, "H", 90.0, 1.90))
