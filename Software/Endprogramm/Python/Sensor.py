import time
import grovepi
class Sensor:
    def __init__(self,pin_id:int, sensor_id:int):
        self.pin_id = pin_id
        self.sensor_id = sensor_id
        self.is_analog = True

    def get_value(self):
        return -1
    def get_location(self):
        if self.is_analog:
            return "A" + str(self.pin_id-14)
        else:
            return "D" + str(self.pin_id)

class LightSensor(Sensor):

    def __init__(self,pin_id:int, sensor_id:int):
        super().__init__(pin_id, sensor_id)
        self.is_analog = True
    def get_value(self):
        grovepi.pinMode(self.pin_id, "INPUT")
        try:
            print("test")
            return grovepi.analogRead(self.pin_id)
        except IOError:
            print("Error")


class DistanceSensor(Sensor):

    def __init__(self,pin_id:int, sensor_id:int):
        super().__init__(pin_id, sensor_id)
        self.is_analog = False

    def get_value(self):
        grovepi.pinMode(self.pin_id, "INPUT")
        try:
            return grovepi.digitalRead(self.pin_id)
        except IOError:
            print("Error")