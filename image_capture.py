from picamera import PiCamera
from time import sleep
import datetime
import os

camera = PiCamera()
camera.resolution = (1024, 768)

path = os.getcwd()
folder = ''
img_ext = '.jpg'

stop_time = datetime.datetime(2021, 4, 25, 20, 30, 0)

folder = '/' + str(stop_time.date())

os.mkdir(path + folder)

i = 0
while True:
    name = '/' + str(i).zfill(4)
    camera.capture(path + folder + name + img_ext)
    curr_time = datetime.datetime.now()
    if curr_time < stop_time:
        i += 1
        sleep(180)
    else:
        exit()
    
