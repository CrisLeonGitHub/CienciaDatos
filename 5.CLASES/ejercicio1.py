class Estudiante:
    def __init__(self, nombre , edad , grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'Estas estudiando {self.nombre}')
        
nombre = input("digame su nombre:")
edad = input("digame su edad:")
grado = input("digame su grado:")

estudiante = Estudiante(nombre,edad,grado)
estudiante.estudiar()