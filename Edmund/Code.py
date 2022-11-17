from picamera import PiCamera
import time
import RPi.GPIO as GPIO

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
time.sleep(5)
p.stop

def run():
#0 degrees
    print("taking picture of 0 degrees")
    camera = PiCamera()
    time.sleep(8)

    camera.capture("/home/pi/Desktop/Edmund's project/Pics0/img.jpg")
    camera.close()
    print("done.")
#90 degrees
    p.ChangeDutyCycle(4+(11.25)/18)
    time.sleep(1)
    p.ChangeDutyCycle(0)
    
    print("taking picture of 45 degrees")
    time.sleep(8)

    camera.capture("/home/pi/Desktop/Edmund's project/Pics90/img.jpg")
    camera.close()
    print("done.")
#45 degrees
    p.ChangeDutyCycle(4+(11.25/18))
    time.sleep(1)
    p.ChangeDutyCycle(0)
    
    print("taking picture of 90 degrees")
    time.sleep(8)

    camera.capture("/home/pi/Desktop/Edmund's project/Pics45/img.jpg")
    camera.close()
    print("done.")
#135 degrees
    p.ChangeDutyCycle(4+(11.25/18))
    time.sleep(1)
    p.ChangeDutyCycle(0)
    
    print("taking picture of 135 degrees")
    time.sleep(8)

    camera.capture("/home/pi/Desktop/Edmund's project/Pics135/img.jpg")
    camera.close()
    print("done.")
    return
camera=PiCamera()
camera.start_preview()
time.sleep(10)
print("ready")
camera.stop_preview()
camera.close
run()
p.stop
