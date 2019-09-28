from sense_hat import SenseHat
sensehat = SenseHat()

# colors
white = (255, 255, 255)  # white 
red = (255, 0, 0)  # red 
green = (0, 255, 0)  # green 
blue = (0, 0 , 255)  # blue 

sensehat.set_pixel(0,0,red)
sensehat.set_pixel(7,0,white)
sensehat.set_pixel(0,7,blue)
sensehat.set_pixel(7,7,green)

# random positions 
from sense_hat import SenseHat
sensehat = SenseHat()

sensehat.clear()
# colors
white = (255, 255, 255)  # white 
red = (255, 0, 0)  # red 
green = (0, 255, 0)  # green 
blue = (0, 0 , 255)  # blue 

# random positions 
from random import randint
while True:
  position1 = (randint(0,7),randint(0,7))
  position2 = (randint(0,7),randint(0,7))
  position3 = (randint(0,7),randint(0,7))
  position4 = (randint(0,7),randint(0,7))
  if position1 != position2 != position3 != position4:
    break 
sensehat.set_pixel(position1[0],position1[1], white)
sensehat.set_pixel(position2[0],position2[1], red)
sensehat.set_pixel(position3[0],position3[1], green)
sensehat.set_pixel(position4[0],position4[1], blue)
