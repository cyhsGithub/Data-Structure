def quick(li, low, high):
    l = low
    h = high
    if low < high:
        pivot = li[low]
        while low < high:
            while low < high and li[high]>pivot:
                high -= 1
            if low < high:
                li[low] = li[high]
                low += 1
            while low < high and li[low]<=pivot:
                low += 1
            if low < high:
                li[high] = li[low]
                high -= 1
        li[low] = pivot
        quick(li, l, low-1)
        quick(li, low +1, h)

li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
quick(li,0,len(li)-1)
print(li)