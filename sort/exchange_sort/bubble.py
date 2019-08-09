#O(n ** 2), stable
def bubble(li):
    for i in range(len(li)-1):
        for j in range(0,len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
bubble(li)
print(li)