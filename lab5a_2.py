from sense_hat import SenseHat
from random import randint
from time import sleep
sensehat = SenseHat()

while True: 
    sensehat.set_pixel(0,0,(randint(0,255),randint(0,255),randint(0,255)))
    sensehat.set_pixel(7,0,(randint(0,255),randint(0,255),randint(0,255)))
    sensehat.set_pixel(0,7,(randint(0,255),randint(0,255),randint(0,255)))
    sensehat.set_pixel(7,7,(randint(0,255),randint(0,255),randint(0,255)))
    sleep(5)
    sensehat.clear()