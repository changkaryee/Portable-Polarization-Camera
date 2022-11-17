from __future__ import division
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

#for ZERO

I = Image.open('/home/pi/Desktop/Edmunds project/Pics0/zero.jpg')
#image proccessing for zero
I1 =I.convert('L')

#Matrix
print(I1.size, I1.mode, I1.format)
I1.save('/home/pi/Desktop/Edmunds project/Pics0/zero_gray.tif')
azero = np.asarray(I1,dtype=np.float32)
#Image.fromarray(azero.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Pics0/test0.jpg")

#writing 0 array in matrix text file
with open("/home/pi/Desktop/Edmunds project/Pics0/Matrix 0","w") as tzero:
    for item in azero:
        tzero.write("%s\n" % item)
        
#for ninety

I = Image.open("/home/pi/Desktop/Edmunds project/Pics90/ninety.jpg")

#Image proccessing for ninety

I2 = I.convert('L')

#Matrix

print(I2.size, I2.mode, I2.format)
I2.save('/home/pi/Desktop/Edmunds project/Pics90/ninety_gray.tif')
aninety = np.asarray(I2,dtype=np.float32)
# Image.fromarray(azero.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Pics90/test0.jpg")

#writing 90 array in matrix text file
with open("/home/pi/Desktop/Edmunds project/Pics90/Matrix 90","w") as tninety:
    for item in aninety:
        tninety.write("%s\n" % item)
        
#for hundredthirtyfive

I = Image.open("/home/pi/Desktop/Edmunds project/Pics135/hundredthirtyfive.jpg")

#Image proccessing for hudredthirtyfive

I3 = I.convert('L')

#Matrix

print(I3.size, I3.mode, I3.format)
I3.save('/home/pi/Desktop/Edmunds project/Pics135/hundredthirtyfive_gray.tif')
ahundredthirtyfive = np.asarray(I3,dtype=np.float32)
# Image.fromarray(azero.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Pics90/test0.jpg")

#writing 135 array in matrix text file
with open("/home/pi/Desktop/Edmunds project/Pics135/Matrix 135","w") as thundredthirtyfive:
    for item in ahundredthirtyfive:
        thundredthirtyfive.write("%s\n" % item)

#for FOURTYFIVE

I = Image.open('/home/pi/Desktop/Edmunds project/Pics45/fourtyfive.jpg')
#image proccessing for zero
I4 =I.convert('L')

#Matrix
print(I4.size, I4.mode, I4.format)
I4.save('/home/pi/Desktop/Edmunds project/Pics45/fourtyfive_gray.tif')
afourtyfive = np.asarray(I4,dtype=np.float32)
#Image.fromarray(azero.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Pics0/test0.jpg")

#writing 45 array in matrix text file
with open("/home/pi/Desktop/Edmunds project/Pics45/Matrix 45","w") as tfourtyfive:
    for item in afourtyfive:
        tfourtyfive.write("%s\n" % item)
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
S0 = normalize(S0)
Image.fromarray(S0.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/S0.jpg")
with open("/home/pi/Desktop/Edmunds project/Matrix S0","w") as Stokes0:
    for item in S0:
        Stokes0.write("%s\n" % item)
#Looking for S1
S1 = azero-aninety
S1=normalize(S1)
Image.fromarray(S1.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/S1.jpg")
with open("/home/pi/Desktop/Edmunds project/Matrix S1","w") as Stokes1:
    for item in S1:
        Stokes1.write("%s\n" % item)
#Looking for S2:
S2 = afourtyfive-ahundredthirtyfive
S2 = normalize(S2)
Image.fromarray(S2.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/S2.jpg")
with open("/home/pi/Desktop/Edmunds project/Matrix S2","w") as Stokes2:
    for item in S2:
        Stokes2.write("%s\n" % item)
#Looking for DOLP
DOLP = S1**2+S2**2
DOLP = normalize(DOLP)
DOLP = DOLP/S0
DOLP = np.sqrt(DOLP)


Image.fromarray(DOLP.astype(np.uint8)).save("/home/pi/Desktop/Edmunds project/Final.jpg")
with open("/home/pi/Desktop/Edmunds project/Matrix Dolp","w") as D:
    for item in DOLP:
        D.write("%s\n" % item)