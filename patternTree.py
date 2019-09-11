# pattern drawing

width = int(input("Please input the width:"))

# upper part
for i in range(1, width):  # range(): index 
    for j in range(i):      # range(): counter 
        print('*',end='')
##    print(i*'*')
    print()
# middle part
for i in range(width):
    print('*',end='')
print()
# bottom part
for i in range(width-1,0,-1):
    for j in range(i):
        print('*',end='')
    print()
