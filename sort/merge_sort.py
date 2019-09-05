# nlogn, 稳定
def merge_sort(li):
    if len(li) <= 1:
        return li

    mid = len(li) // 2
    l1 = merge_sort(li[:mid])
    l2 = merge_sort(li[mid:])
    l = merge(l1,l2)
    return l

def merge(l1, l2):
    index1 = len(l1) - 1
    index2 = len(l2) - 1
    l1.extend([0 for i in range(len(l2))])

    while index2 >= 0:
        if index1 < 0:
            l1[:index2+1] = l2[:index2+1]
            break
        if l1[index1] < l2[index2]:
            l1[index1 + index2 + 1] = l2[index2]
            index2 -= 1
        else:
            l1[index1 + index2 + 1] = l1[index1]
            index1 -= 1
    return l1


li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
li = merge_sort(li)
print(li)