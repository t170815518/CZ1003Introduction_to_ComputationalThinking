from sense_hat import SenseHat
sense = SenseHat()

while True:
    breaker = input("enter 'quit' to exit the program, type other strings to change color")
    if breaker == 'quit':
        break 
    # input
    while True:
    # avoid bugs
        try: 
            color_msg_str = input("Type the color of the message(e.g. 255,255,0): ")
            color_msg=tuple(int(i) for i in color_msg_str.split(','))
            color_bg_str = input("Type the color of the background(e.g. 0,0,255): " )
            color_bg=tuple(int(i) for i in color_bg_str.split(','))
            # user-friendly confirmation 
            if color_msg == color_bg:
                confirmation = input("The color of the background and text seems to be the same. Enter 'yes' to confirm your choices, 'no' to change the color: ")
                if confirmation == 'no':
                    continue 
            break 
        except:
            print("Please follow the syntax: 255,255,0")
    while True:  # do-while structure 
        speed = input("Type the scroll speed(e.g. speed=0.5):")
        if speed.isnumeric():
            speed = float(speed)
            break
        else:
            print("Please print a more appropriate value!")
    message = input("Type the message:")
    sense.set_rotation(180)
    sense.show_message(message, text_colour = color_msg,\
                                   back_colour = color_bg,\
                                   scroll_speed = speed)
