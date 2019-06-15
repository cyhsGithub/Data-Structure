#avg O(n ** 5/4), worst O(n ** 2)
#not stable,在分块排序的时候，相同的数可能从后面跑到前面
def shell(li):
    delta = [5,3,1]
    for i in delta:
        li = shell_insertionSort(li,i)

    return li

def shell_insertionSort(li,delta):
    for i in range(delta,len(li),delta):
        while True:
            if i - delta < 0:
                break

            if li[i] < li[i-delta]:
                li[i], li[i - delta] = li[i - delta], li[i]
                i -= delta
            else:
                break

    return li

li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
li = shell(li)
print(li)