from Sensor import Sensor, LightSensor, DistanceSensor
if __name__ == "__main__":
    s1 = LightSensor(14, 0)
    s2 = DistanceSensor(4, 0)
    while True:
        print(s1.get_location() + " : " + str(s1.get_value()))
        print(s2.get_location() + " : " + str(s2.get_value()))