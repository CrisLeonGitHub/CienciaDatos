class Persona:
    def __init__(self,nombre,edad):
        self.nombre= nombre
        self.edad= edad
        
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)
    
cris = Persona("Cris", 50)
juan = Persona("Juan", 47)
yuyi = Persona("yuyi", 40)
print(cris)
print(repr(cris))

nueva_persona = cris + juan + yuyi
print(nueva_persona.nombre)