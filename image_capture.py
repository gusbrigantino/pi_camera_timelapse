from picamera import PiCamera
from time import sleep
import datetime
import os

camera = PiCamera()
camera.resolution = (1024, 768)

path = os.getcwd()
folder = ''
img_ext = '.jpg'

stop_time = datetime.datetime(2021, 4, 24, 20, 0, 0)

folder = '/' + str(stop_time.date())

i = 0
while True:
    name = '/' + str(i).zfill(4)
    camera.capture(path + name + img_ext)
    curr_time = datetime.datetime.now()
    if curr_time < stop_time:
        i += 1
        sleep(3)
    else:
        exit()
    
