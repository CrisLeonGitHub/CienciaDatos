class Gato():
    def sonido(self):
        return "miau"
    
class Perro():
    def sonido(self):
        return "guau"

def hacer_sonido(animal):
    print(animal.sonido())
    
cat = Gato()
dog = Perro()

hacer_sonido(cat)
hacer_sonido(dog)