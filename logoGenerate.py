from sense_hat import SenseHat
sensehat = SenseHat()

sensehat.clear()
color_list = [(4,104,255),(16,187,251),(28,248,237),(39,245,167),(51,242,107)
,(67,239,62),(131,237,72),(187,235,83)]
marker = (255,0,0)

# create the matrix 
imageLists = [[] for i in range(8)]
for i in range(8):
    imageLists[i] = [(0,0,0) for j in range(8)]
# set the background
for i in range(8):
  for j in range(8):
    imageLists[i][j] = color_list[i]

# integrate the matrix 
image_pixels = []
for (i,j) in [(1,0),(1,1),(2,1),(3,1),(5,1),(4,1),(6,2),
(5,3),(4,4),(3,4),(2,4),(1,4),(5,5),(6,6),(5,7),(4,7),(3,7),(2,7),(1,7)]:
  imageLists[i][j] = marker
for i in range(8):
    image_pixels.extend(imageLists[i])
# image_pixels = [b, b, b, b, b, b, b, b,
#                 w, w, b, b, w, b, b, w,
#                 b, w, b, b, w, b, b, w,
#                 b, w, b, b, w, b, b, w,
#                 b, w, b, b, w, b, b, w,
#                 b, w, b, w, b, w, b, w,
#                 b, b, w, b, b, b, w, b,
#                 b, b, b, b, b, b, b, b]
sensehat.set_pixels(image_pixels)
