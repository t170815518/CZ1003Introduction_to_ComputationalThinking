def bubble_sort(l):
    # to_sort = l, l is changed
    to_sort = l.copy()
    for i in range(len(to_sort)):
        swapped = True
        for j in range(len(to_sort)-i-1):  # from the beginning 
            if to_sort[j] > to_sort[j+1]:
                to_sort[j], to_sort[j+1] = to_sort[j+1], to_sort[j]
                swapped = False
        if swapped:
            return to_sort


if __name__=='__main__':
    l = [5,7,9,3,1,2,3,0,-1,-3,5,2,1,5,6]
    s = bubble_sort(l)
    print("before sort: ", l)
    print('After sort: ', s)
