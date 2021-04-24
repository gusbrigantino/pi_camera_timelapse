import os
import cv2
import numpy as np
import datetime
from os.path import isfile, join

path = os.getcwd()
images_folder = '/lapse_test'
out_file = 'lapses/time_lapse_'
vid_ext = '.mov'

fps = 10.0
today = datetime.date.today().strftime("%m_%d_%Y")

img_files = [x for x in os.listdir(path + images_folder) if isfile(join(path + images_folder, x))]
img_files = sorted(img_files)
size = (0, 0)


image_array = []
first  = True
for img_file in img_files:
    full_img_file = path + images_folder + '/' + img_file
    image = cv2.imread(full_img_file)

    if first:
        h, w, l = image.shape
        size = (w, h)
        first = False

    image_array.append(image)

out = cv2.VideoWriter(out_file + today + vid_ext, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for x in image_array:
    out.write(x)
out.release()
print("Success")