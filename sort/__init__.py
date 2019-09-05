def merge(l1, l2):
    index1 = len(l1)-1
    index2 = len(l2)-1
    l1.extend([0 for i in range(len(l2))])
    while index1 >= 0:
        if index2 < 0:
            break
        if l1[index1] >= l2[index2]:
            l1[index1+index2+1] = l1[index1]
            index1 -= 1
        else:
            l1[index1 + index2 + 1] = l2[index2]
            index2 -= 1
    print(l1)
    return l1

print(merge([1, 5, 8], [0, 123]))