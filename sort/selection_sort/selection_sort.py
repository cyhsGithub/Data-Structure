#每次把一个元素放到正确的位置上，这里是每次选最小的
#O(n ** 2)
#unstable,本例中如果0在第二个1后面，第一个1会被交换到第二个1后面

def selection_sort(li):
    for n in range(len(li)):
        s = n
        for i in range(n, len(li)):
            if li[i] < li[s]:
                s = i
        li[s],li[n] = li[n],li[s]

    # return li

# def selection(li):
#     for i in range(len(li)):
#         for n in range(len(li)-1, i, -1):
#             if li[n] < li[n-1]:
#                 li[n],li[n-1] = li[n-1],li[n]
#     return li

li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
selection_sort(li)
print(li)