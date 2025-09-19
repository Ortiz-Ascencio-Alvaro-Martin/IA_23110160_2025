class Usuario:
    # Atributos de instancia
    def __init__(self, nombre, apellidos,
                edad, direccion, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    # Métodos
    def iniciar_sesion(self):
        print(f"El usuario {self.nombre} {self.apellidos} ha iniciado sesión")
# Instancias
usuario_1 = Usuario("Alvaro", "Ortiz Ascencio",
                    22, "mi casa",
                    "33 xx xx xx xx")
usuario_2 = Usuario("Angela", "López Macedp",
                    23, "Sin dirección",
                    "322 xxx xx xx")

usuario_1.iniciar_sesion()
usuario_2.iniciar_sesion()