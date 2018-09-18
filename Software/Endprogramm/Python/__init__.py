from Sensor import Sensor, LightSensor, DistanceSensor
if __name__ == "__main__":
    s1 = LightSensor(14, 0)
    s2 = DistanceSensor(4, 0)
    print(s1.get_location())
    print(s2.get_location())