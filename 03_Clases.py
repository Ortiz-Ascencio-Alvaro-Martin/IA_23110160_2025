# Declaración de clase
class Carro():
    # Atributos de clase
    atributo_1 = "valor 1"
    atributo_2 = "valor 2"

    # Métodos
    def metodo_1(self):
        print("Método de clase")
    def metodo_2(self):
        print("Método de clase")

# Se declara la clase vehiculo
class Vehiculo():
    # Atributos
    color = None
    longitud_metros = None
    ruedas = 4

    # Métodos
    def arrancar(self):
        print("El motor ha arrancado.")

    def detener(self):
        print("El motor está detenido.")

texto = "Python: El poder de los objetos."
print(type(texto))

mayusculas = texto.upper()
print(mayusculas)