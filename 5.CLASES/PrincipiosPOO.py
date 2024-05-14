#SRP
class TanqueCon:
    def __init__(self):
        self.combustible =100
    
    def agregar(self,cant):
        self.combustible += cant
        
    def usar(self,canti):
        self.combustible -=canti
    
    def obtener(self):
        return self.combustible
                
class Auto:
    def __init__(self, tanque):
        self.pos = 0
        self.tanque = tanque
        
    def mover(self,distan):
        if self.tanque.obtener() >= distan/2:
            self.pos +=distan
            self.tanque.usar(distan/2)
            print("se movio")
        else:
            print("No se movio")
            
    def obt_pos(self):
        return self.pos
    
tanq = TanqueCon()
auti = Auto(tanq)
print(auti.obt_pos())
auti.mover(10)
print(auti.obt_pos())
auti.mover(100)
print(auti.obt_pos())
auti.mover(100)
print(auti.obt_pos())


#OCP
class Notificador:
    def __init__(self, usuario , mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando por mail a {self.usuario.mail}")
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando por SMS a {self.usuario.sms}")
        
class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviando por WhatsApp a {self.usuario.WhatsApp}")
        
#LSP
class Aves():
    pass

class AvesVoladoras(Aves):
    def volar(self):
        print("Puedo volar")

class AvesNoVoladoras(Aves):
    pass

#ISP
from abc import ABC, abstractmethod
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
    
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador,Durmiente,Comedor):
    def comer(self):
        print("el humano comer")
        
    def trabajar(self):
        print("el humano trabaja")
        
    def dormir(self):
        print("el humano duerme")

class Robot(Trabajador):       
    def trabajar(self):
        print("el robot esta trabaja")


robot = Robot()
hum = Humano()

robot.trabajar()
hum.trabajar()
hum.dormir()

#DIP
