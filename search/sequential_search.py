#O(n)
def seq(li,key):
    for i,v in enumerate(li):
        if v == key:
            return (i,v)
    return "Not Found!"

if __name__ == '__main__':
    li = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    result = seq(li,300)
    print(result)


