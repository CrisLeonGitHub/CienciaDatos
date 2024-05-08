class Persona:
    def __init__(self, nombre , edad , nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f"hola estoy hablando {self.nombre}")
        
class Empleado(Persona):
    def __init__(self, nombre , edad , nacionalidad,trabajo , salario ):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

ems = Empleado("Cris",23,"chileno","teachleader",2200000)
ems.hablar()