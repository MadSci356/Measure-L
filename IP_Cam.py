from SimpleCV import *
from pygame import error as pg_err #just so pygame error is not invoked
from time import sleep

ip_cam = JpegStreamCamera("http://192.168.1.147:8080/video")
disp = Display()


try:
    while disp.isNotDone():
        img = ip_cam.getImage()
        img.save(disp)
        time.sleep(.01)
except pg_err:
    pass
