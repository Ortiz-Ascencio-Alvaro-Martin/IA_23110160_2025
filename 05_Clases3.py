class Usuario:
    def __init__(self, nombre, apellidos, edad, direccion, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
    # Atributos
    nombre = "Sin nombre"
    apellidos = "Sin apellidos"
    edad = 0
    direccion = "Sin dirección"
    telefono = "Sin teléfono"

    # Métodos
    def iniciar_sesion(self):
        print("El usuario ha iniciado sesión")

    def cerrar_sesion(self):
        print("El usuario ha cerrado sesión")

    def cambiar_nombre_perfil(self):
        print("Se cambió el nombre")
        # Instanciación
# usuario_1 = Usuario()

# # Inicialización de datos
# usuario_1.nombre = "Alvaro"
# usuario_1.apellidos = "Ortiz Ascencio"
# usuario_1.edad = 22
# usuario_1.direccion = "C/Programación Fácil n.º 34"
# usuario_1.telefono = "23110160"
# Instancia
usuario_1 = Usuario("Alvaro",
                    "Ortiz Ascencio",
                    22,
                    "C/Programación Fácil n.º 34",
                    "23110160")

# Probamos un atributo
print(usuario_1.nombre)
# Instancia
#usuario_1 = Usuario(nombre = "Martin") esto marca error