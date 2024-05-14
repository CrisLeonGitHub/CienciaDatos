class Celular:
    def __init__(self, marca , modelo , camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f'Estas haciendo una llamada desde un :{self.modelo}')
        
    def cortar(self):
        print(f'Estas cortando desde un :{self.modelo}')
    
celular1 = Celular("Huawei","p30pro","48MP")

print(celular1.marca)
celular1.llamar()