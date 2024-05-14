from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre , edad , sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
        
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy trabajando como: {self.actividad}")
        
estu = Estudiante("Juan", 23,"Masculino","objetos")
trabaja = Trabajador("Cris", 50,"Masculino","Teach Leader")

estu.hacer_actividad()
trabaja.hacer_actividad()


