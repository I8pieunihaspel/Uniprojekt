import RPi.GPIO as GPIO
import time
class Motor(object):
    def __init__(self, id: int, location:str):
        self.id:int = id
        self.location: str = location
        self.output: int = 0
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.id, GPIO.OUT)

    def drive(self, power: int):
        pass

    def show_alive(self):
        for i in range(100):
            GPIO.output(7, True)
            time.sleep(0.1)

    def get_location(self):
        return self.location

