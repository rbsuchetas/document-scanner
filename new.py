import cv2
import numpy


#from VideoCapture import Device
cam = cv2.VideoCapture(0)
cam.saveSnapshot('image.jpg')
