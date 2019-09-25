classes = dict()
num_class = int(input("Input the number of classes: "))
for i in range(num_class):
    name_class = input("Input the name of class {}: ".format(i+1))
    tmp_list = []
    for j in range(40):
        # tmp_list[j] = float(input("Input the score of student {}: ".format(j+1))) ERROR: out of range
        score = float(input("Input the score of student {}: ".format(j+1)))
        tmp_list.append(score)
    classes[name_class] = tmp_list  # dictionary syntax, the index is the key 

print(classes)