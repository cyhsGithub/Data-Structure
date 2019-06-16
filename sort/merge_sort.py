def merge_sort(li):
    if len(li) <= 1:
        return li

    mid = len(li) // 2
    l1 = merge_sort(li[:mid])
    l2 = merge_sort(li[mid:])
    l = merge(l1,l2)
    return l

def merge(l1,l2):
    result = []
    length = len(l1) + len(l2)
    while len(result) < length:
        if len(l1) == 0:
            result = result + l2
        elif len(l2) == 0:
            result = result + l1
        elif l1[0] < l2[0]:
            result.append(l1.pop(0))
        elif l2[0] < l1[0]:
            result.append(l2.pop(0))
        elif l2[0] == l1[0]:
            result.append(l1.pop(0))
            result.append(l2.pop(0))
    return result

li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
li = merge_sort(li)
print(li)