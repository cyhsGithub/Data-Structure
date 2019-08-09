#avg O(n ** 5/4), worst O(n ** 2)
#not stable,在分块排序的时候，相同的数可能从后面跑到前面
def shell(li):
    delta = [5,3,1]
    for i in delta:
        shell_insertionSort(li,i)


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

# def shell(li):
#     delta = [5,3,1]
#
#     for d in delta:
#         for i in range(d, len(li), d):
#             for n in range(i, 0, -d):
#                 if li[n] < li[n-d]:
#                     li[n], li[n - d] = li[n - d], li[n]
#
#     return li
li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
shell(li)
print(li)