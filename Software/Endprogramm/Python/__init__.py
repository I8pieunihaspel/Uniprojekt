from Sensor import Sensor, LightSensor, DistanceSensor
from Motor import Motor

def test_sensors():
    s1 = LightSensor(14, 0)
    s2 = DistanceSensor(4, 0)
    while True:
        print(s1.get_location() + " : " + str(s1.get_value()))
        print(s2.get_location() + " : " + str(s2.get_value()))

def test_motors():
    ms = []
    ms.append(Motor(7, "test"))
    ms.append(Motor(8, "test"))
    ms.append(Motor(9, "test"))
    ms.append(Motor(10, "test"))
    for m in ms:
        m.show_alive()

if __name__ == "__main__":
    test_motors()