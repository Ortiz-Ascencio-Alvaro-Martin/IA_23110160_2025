# # Declaración de clase
# class NombreClase():
#     pass

# # Objeto creado a partir de la clase
# objeto = NombreClase()
from datetime import datetime
# Declaración de clase
class NombreClase():
    # Atributos de clase
    atributo_1 = "valor 1"
    atributo_2 = "valor 2"

    # Método
    def metodo_1(self):
        print("Método llamado con el objeto.")
    def metodo_prueba(self):
        print(datetime.now())


# Objeto creado a partir de la clase
objeto = NombreClase()

# Llamada al método
objeto.metodo_1()
objeto.metodo_prueba()
print(objeto)
print(objeto.atributo_1)