from picamera import PiCamera
from time import sleep
from tkinter import *
import cv2
import sys
import picamera.array

        
def displayAtThinter():
    camera.resolution=(640,480)
    camera.sharpness = 10
    camera.contrast = 30
    camera.vflip=False
    camera.hflip=False
    camera.exposure_mode = 'auto'
    root = Tkinter.Tk() 
    b,g,r = cv2.split(img) 
    img2 = cv2.merge((r,g,b))
    img2FromArray = Image.fromarray(img2)
    imgtk = ImageTk.PhotoImage(image=img2FromArray) 
    Tkinter.Label(root, image=imgtk).pack() 
    root.mainloop()
    
capturePiCam()
displayAtThinter()
