from __future__ import division
from picamera import PiCamera
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from time import sleep


camera = PiCamera()
count = 0
def run():
    camera.start_preview()
    sleep(15)
    camera.stop_preview()
    check = input("\nReady for 0?:")
    if check == "yes" or "y":
        camera.capture("/home/pi/Desktop/Edmunds project/Pics0/zero.jpg")
        print("done with 0.")
    check = input("\nReady for 90?:")
    if check == "yes" or "y":
        camera.capture("/home/pi/Desktop/Edmunds project/Pics90/ninety.jpg")
        print("done with 90.")
    check = input("\nReady for 135?:")
    if check == "yes" or "y":
        camera.capture("/home/pi/Desktop/Edmunds project/Pics135/hundredthirtyfive.jpg")
        print("done with 135.")
    check = input("\nReady for 45?:")
    if check == "yes" or "y":
        camera.capture("/home/pi/Desktop/Edmunds project/Pics45/fourtyfive.jpg")
        print("done with 45.")
    camera.close()
run()
#for ZERO
camera.close()
I = Image.open('/home/pi/Desktop/Edmunds project/Pics0/zero.jpg')
#image proccessing for zero
I1 =I.convert('L')

#Matrix
I1.save('/home/pi/Desktop/Edmunds project/Pics0/zero_gray.tif')
azero = np.asarray(I1,dtype=np.float32)
#Image.fromarray(azero.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Pics0/test0.jpg")

#writing 0 array in matrix text file
with open("/home/pi/Desktop/Edmunds project/Pics0/Matrix 0","w") as tzero:
    for item in azero:
        tzero.write("%s\n" % item)

print("Matrix for 0 done")
#for ninety

I = Image.open("/home/pi/Desktop/Edmunds project/Pics90/ninety.jpg")

#Image proccessing for ninety

I2 = I.convert('L')

#Matrix

I2.save('/home/pi/Desktop/Edmunds project/Pics90/ninety_gray.tif')
aninety = np.asarray(I2,dtype=np.float32)
# Image.fromarray(azero.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Pics90/test0.jpg")

#writing 90 array in matrix text file
with open("/home/pi/Desktop/Edmunds project/Pics90/Matrix 90","w") as tninety:
    for item in aninety:
        tninety.write("%s\n" % item)
print("Matrix for 90 done")
#for hundredthirtyfive

I = Image.open("/home/pi/Desktop/Edmunds project/Pics135/hundredthirtyfive.jpg")

#Image proccessing for hudredthirtyfive

I3 = I.convert('L')

#Matrix

I3.save('/home/pi/Desktop/Edmunds project/Pics135/hundredthirtyfive_gray.tif')
ahundredthirtyfive = np.asarray(I3,dtype=np.float32)
# Image.fromarray(azero.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Pics90/test0.jpg")

#writing 135 array in matrix text file
with open("/home/pi/Desktop/Edmunds project/Pics135/Matrix 135","w") as thundredthirtyfive:
    for item in ahundredthirtyfive:
        thundredthirtyfive.write("%s\n" % item)

print("Matrix for 135 done")
#for FOURTYFIVE

I = Image.open('/home/pi/Desktop/Edmunds project/Pics45/fourtyfive.jpg')
#image proccessing for zero
I4 =I.convert('L')

#Matrix
I4.save('/home/pi/Desktop/Edmunds project/Pics45/fourtyfive_gray.tif')
afourtyfive = np.asarray(I4,dtype=np.float32)
#Image.fromarray(azero.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Pics0/test0.jpg")

#writing 45 array in matrix text file
with open("/home/pi/Desktop/Edmunds project/Pics45/Matrix 45","w") as tfourtyfive:
    for item in afourtyfive:
        tfourtyfive.write("%s\n" % item)
print("Matrix for 45 done")
#Normalize Function
def normalize(I):
    mn = I.min()
    mx = I.max()
    mx = mx-mn
    
    I = ((I-mn)/mx) * 255
    return I.astype(np.uint8)

#Looking for S0
S0 = azero+aninety+ahundredthirtyfive+afourtyfive
S0 = np.divide(S0,2)
Image.fromarray(normalize(S0).astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/S0.jpg")
with open("/home/pi/Desktop/Edmunds project/Matrix S0","w") as Stokes0:
    for item in S0:
        Stokes0.write("%s\n" % item)
print("S0 done")
#Looking for S1
S1 = azero-aninety
Image.fromarray(normalize(S1).astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/S1.jpg")
with open("/home/pi/Desktop/Edmunds project/Matrix S1","w") as Stokes1:
    for item in S1:
        Stokes1.write("%s\n" % item)
print("S1 done")
#Looking for S2:
S2 = afourtyfive+ahundredthirtyfive
Image.fromarray(normalize(S2).astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/S2.jpg")
with open("/home/pi/Desktop/Edmunds project/Matrix S2","w") as Stokes2:
    for item in S2:
        Stokes2.write("%s\n" % item)
print("S2 done")
#Looking for DOLP
DOLP = S1 * S1 + S2 * S2
#Image.fromarray(DOLP.astype(np.uint8)).show()
DOLP = np.sqrt(DOLP)

#Image.fromarray(DOLP.astype(np.uint8)).show()
DOLP = (DOLP)/(S0+1)
#Image.fromarray(DOLP.astype(np.uint8)).show()


Image.fromarray(normalize(DOLP).astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Dolp.jpg")
with open("/home/pi/Desktop/Edmunds project/Matrix Dolp","w") as D:
    for item in DOLP:
        D.write("%s\n" % item)

print("DOLP done")
