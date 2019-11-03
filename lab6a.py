def get_color():
    # color is an RGB value in string, e.g # 255,1,0
    color = input("Type the color in string(e.g. 255,1,0)")
    Try = 1 
    while True:
        if Try != 1:
            color = input("Type the color in string(e.g. 255,1,0)")
        elif Try == 3: 
            print("Too many attempts, 0 is returned by default.")
            return 0
        try:
            color_list = [int(x) for x in color.split(',')]
            if [x for x in color_list if not 0<=x<=255]:
                print("The RGB value should be within [0,255]. Try again.({}/3)".format(Try))
                Try += 1
        except:
            print("Please type the proper integer value.({}/3)".format(Try))
            Try += 1 
        else:
            return color_list[0], color_list[1], color_list[2] 

if '__name__' == '__main__':
    color = input("Type the color in string(e.g. 255,1,0)")
    r,g,b = get_color(color)
