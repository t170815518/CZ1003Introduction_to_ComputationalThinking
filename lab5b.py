from sense_hat import SenseHat
sense = SenseHat()

red = (255,0,0)
white = (255,255,255)
blue = (0,0,255)

# image_pixels = [b, b, b, b, b, b, b, b,
#                 b, b, b, y, b, b, b, b,
#                 b, b, y, y, y, b, b, b,
#                 b, y, b, y, b, y, b, b,
#                 b, b, b, y, b, b, b, b,
#                 b, b, b, b, y, b, b, b,
#                 b, b, b, y, b, b, b, b,
#                 b, b, b, b, b, b, b, g]

# initialize 
imageLists = [[] for i in range(8)]
image_pixels = []
for i in range(8):
    imageLists[i] = [white for j in range(8)]

for i in range(4):
    for j in range(4):
        imageLists[i][j] = red
for i in range(4,8):
    for j in range(4,8):
        imageLists[i][j] = blue 
for i in range(8):
    image_pixels.extend(imageLists[i])

sense.set_pixels(image_pixels)