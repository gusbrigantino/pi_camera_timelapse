from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (1024, 768)

for i in range(20):
    camera.capture('/home/pi/Pictures/image' + str(i) + '.jpg')
    sleep(1)
