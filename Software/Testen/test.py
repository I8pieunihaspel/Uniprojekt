import time
import grovepi

sensor = 14

grovepi.pinMode(sensor, "INPUT")

while True:
	try:
		print(grovepi.analogRead(sensor))
		time.sleep(0.5)
	except IOError:
		print("Error")
#Test