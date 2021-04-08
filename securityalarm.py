import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep

camera = PiCamera()

GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, 0)
time.sleep(0.2)

print "Starting Measurement"

GPIO.output(TRIG, 1)
time.sleep(0.00001)
GPIO.output(TRIG, 0)

while GPIO.input(ECHO) == 0:
	start = time.time()

while GPIO.input(ECHO) == 1:
	stop = time.time()

cal_time =  (stop - start) * 17000 

if cal_time < 5:
	camera.start_preview()
	sleep(3)
	camera.capture('/home/pi/Desktop/image.jpg')
	camera.stop_preview()
 
print ("distance: ",cal_time," cm") 

GPIO.cleanup()
