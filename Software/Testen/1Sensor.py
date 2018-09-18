import time
import grovepi

sensor = 4

while True:
		try:
			if grovepi.digitalRead(sensor) == 0:
				print("found Something" + ":" + str(sensor))
	
			else:
				print("nothing"+ ":" + str(sensor))
			time.sleep(0.1)
		except IOError:
			print("Error")
#Test