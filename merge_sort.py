def merge_sort(l):
    if len(l) == 1:
        return l
    # left = merge_sort(l[:l // 2])
    # right = merge_sort(l[l // 2:])
    left = merge_sort(l[:len(l)//2])
    right = merge_sort(l[len(l)//2:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i <= len(left)-1 and j <= len(right)-1:
        if left[i] < right[j]:  # TypeError: '<' not supported between instances of 'int' and 'list'--
                                        # be careful about the extend and append
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i <= len(left)-1:
        result.extend(left[i:])
    else:
        result.extend(right[j:])
    return result


if __name__ == '__main__':
    l = [4,1,1,1,1,5,6,2,3,4,5,1,4,7,98,0]
    print('Before: ',l)
    print('After: ', merge_sort(l))
