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

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")
        
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre , edad , nacionalidad,habilidad, salario,empresa):
        Persona.__init__(self, nombre , edad , nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self): 
        return f'{super().mostrar_habilidad()}'
    
ems = Empleado("Cris",23,"chileno","teachleader",2200000)
ems.hablar()

artis = EmpleadoArtista("arjona",34,"la que sea","cantante",23000,"Sony")
artis.presentarse()