##sequence = [1,1]
##length_expection = int(input("Please enter the length\
##                             of Fibonacci to generate:"))
##i = 1
##j = 2 
##while len(sequence) <= length_expection:
##    sequence.append(i+j)
##    i += 1
##    j += 1
##print(element for element in sequence)

a = 1
b = 1
while a < 1000:
    print(a)
    a, b = b, a+b 
