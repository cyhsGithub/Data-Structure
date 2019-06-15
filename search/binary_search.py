#logn, 表必须有序

def bin(li,key):
    low = 0
    high = len(li) - 1
    time = 0
    while low <= high:
        time += 1
        mid = (low + high) // 2
        if key > li[mid]:
            low = mid + 1
        elif key < li[mid]:
            high = mid - 1
        elif key == li[mid]:
            return (mid, time)

    return "Not Found"

if __name__ == '__main__':
    li = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    li.sort()
    print(li)
    result = bin(li,300)
    print(result)

