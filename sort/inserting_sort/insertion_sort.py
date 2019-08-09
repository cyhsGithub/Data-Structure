#O(n ** 2), stable
def insertion_sort(li):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                li[i],li[j] = li[j],li[i]

# def insertion_sort(li):
#     for i in range(1,len(li)):
#         while True:
#             #关键
#             if i - 1 < 0:
#                 break
#
#             if li[i] < li[i-1]:
#                 li[i],li[i-1] = li[i-1],li[i]
#                 i -= 1
#             else:
#                 break
#
#     return li


li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
insertion_sort(li)
print(li)