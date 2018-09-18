import time
import grovepi
class Sensor: #(eigentliche) Abstrakte Klasse, welcher alle Sensoren zugehörig sind 
    def __init__(self,pin_id:int, sensor_id:int): #Konstruktor
        self.pin_id = pin_id #ID, welche man benutzt um die Sensoren anzusprechen
        self.sensor_id = sensor_id #interne ID
        self.is_analog = True #Gibt an ob der Sensor analog oder nicht analog(=digital)
        
    @abstractmethod
    def get_value(self): # Methode welche den Wert des Sensors gibt.
        return -1 #Hier ein placeholder code, weil python keine abstrakten Klassen unterstützt 
    
    def get_location(self): #generiert den Text, welcher auf dem GrovePi steht aus der Pin_id und der is_analog variable.
        if self.is_analog:
            return "A" + str(self.pin_id-14)
        else:
            return "D" + str(self.pin_id)

class LightSensor(Sensor): #Klasse LightSensor erbt von der Klasse Sensor 

    def __init__(self,pin_id:int, sensor_id:int): #Konstruktor
        super().__init__(pin_id, sensor_id) # ruft Konstruktor der Klasse von der geerbt wird auf
        self.is_analog = True # jeder Helligkeitssensor gibt automatisch ein analoges Signal.
        
    def get_value(self): #implementation von get_value ist für alle Helligkeitssensoren gleich, da alle analoge Signale herrausgeben.
        grovepi.pinMode(self.pin_id, "INPUT")#den Pin als Input einstellen
        try:
            return grovepi.analogRead(self.pin_id) #den wert der Helligkeit zwischen 0, 1023 auslesen und returnen 
        except IOError:
            print("Error")


class DistanceSensor(Sensor): #Klasse DistanceSensor erbt von der Klasse Sensor 

    def __init__(self,pin_id:int, sensor_id:int): #Konstruktor
        super().__init__(pin_id, sensor_id) # ruft Konstruktor der Klasse von der geerbt wird auf
        self.is_analog = False # jeder Abstandssensor gibt automatisch ein digitales Signal.

    def get_value(self):
        grovepi.pinMode(self.pin_id, "INPUT") #den Pin als Input einstellen
        try:
            return grovepi.digitalRead(self.pin_id) #den geschätzen Abstand enweder als GPIO.HIGH oder GPIO.LOW aus.
        except IOError:
            print("Error")
