import time
import grovepi

sensoren = []
start = 2
for i in range(4):
	grovepi.pinMode(start+i, "INPUT")
	sensoren.append(start+i)


while True:
	for sensor in sensoren:
		try:
			if grovepi.digitalRead(sensor) == 0:
				print("found Something" + ":" + str(sensor))
	
			else:
				print("nothing"+ ":" + str(sensor))
			time.sleep(0.5)
		except IOError:
			print("Error")
#Test