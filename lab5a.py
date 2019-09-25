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
