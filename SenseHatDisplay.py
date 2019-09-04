from sense_hat import SenseHat
sense = SenseHat()

color_msg_str = input("Type the color of the message(e.g. 255,255,0: ")
color_msg=tuple(int(i) for i in color_msg_str.split(','))
color_bg_str = input("Type the color of the background(e.g. 0,0,255):" )
color_bg=tuple(int(i) for i in color_bg_str.split(','))
speed = float(input("Type the scroll speed(e.g. speed=0.5):"))

sense.set_rotation(180)
sense.show_message("This is fun, and I got it", text_colour = color_msg,\
                               back_colour = color_bg,\
                               scroll_speed = speed)
