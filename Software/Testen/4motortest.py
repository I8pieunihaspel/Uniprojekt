import RPi.GPIO as GPIO
import time

ids = [7,8,9,10]

GPIO.setmode(GPIO.BOARD)
for id in ids:
	GPIO.setup(id, GPIO.OUT)
while True:
	for id in ids:
		GPIO.output(id, True)