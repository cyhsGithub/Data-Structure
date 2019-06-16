#avg O(nlogn), worst O(n ** 2),取决于pivot的选取
#pivot选的好，进行logn次递归（logn层），每层n；
#选的不好，有n层，每层n
#unstable, 选取Pivot时，与pivot值相同的元素会被放到右边
def quick_sort(li):
    if len(li) == 0 or len(li) == 1:
        return li

    pivot = li[len(li) // 2 - 1]
    left = []
    right = []
    li.remove(pivot)
    for i in li:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    l1 = quick_sort(left)
    l2 = quick_sort(right)
    l1.append(pivot)
    return l1 + l2

li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
li = quick_sort(li)
print(li)