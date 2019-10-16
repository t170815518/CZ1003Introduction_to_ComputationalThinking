from sense_hat import SenseHat 
from time import sleep 

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    
    # confusing part 
    if 1<pitch<179 and x!=0:
        new_x -= 1 
    elif 170<pitch<359 and x!=7:
        new_x += 1 
    if 10<roll<179 and y!=7:
        new_y += 1 
    elif 190<roll<359 and y!=0:
        new_y -= 1 
    new_x, new_y = checkwall(x,y,new_x,new_y)
    return new_x, new_y
    
def checkwall(x,y, new_x,new_y):
    if board[new_y][new_x] != q and board[new_y][new_x] != m :
        return new_x, new_y
    elif board[new_y][x] != q and board[new_y][x] != m:
        return x, new_y
    elif board[y][new_x] != q and board[y][new_x] != m:
        return new_x, y
    else:
        return x, y 

def check_target(x,y):
    global board, g
    if board[x][y] == g:
        return True
    
sense = SenseHat()

b = (0,0,0)
m = (0,0,255)
w = (255,255,255)
q = (255,0,0)
g = (255,255,0)
board = [[q,q,q,q,q,q,q,q],
         [q,m,m,m,m,m,m,q],
         [q,m,b,b,b,b,m,q],
         [q,m,b,m,m,b,m,q],
         [q,m,b,m,m,b,m,q],
         [q,m,b,m,g,b,m,q],
         [q,m,w,m,m,m,m,q],
         [q,q,q,q,q,q,q,q]] 
x,y = 2,6
board_1d = sum(board,[])
sense.set_pixels(board_1d)  # convert 2D-list into 1D-ist
#  sense.set_pixels(sum(board,[])) --error 

while True:
    # range of values: both are [0, 360]
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    x, y = move_marble(pitch, roll, x, y)
    board[y][x] = w  # it will leave a trial; why (y,x)?  Because 2-d list! 
    sense.set_pixels(sum(board, []))
    sleep(0.5)
    if check_target(x,y):
        sense.show_message('Game Complete!', text_colour=(255,0,0))
        break 
    
