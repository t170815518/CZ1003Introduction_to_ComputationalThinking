from lab6a import get_color 
from sense_hat import SenseHat 

sense = SenseHat()
r, g, b = get_color()
sense.show_message("Yes...", text_colour = (r,g,b))
