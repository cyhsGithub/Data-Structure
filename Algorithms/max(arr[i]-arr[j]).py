def f(li):
    if li == [] or len(li) == 1:
        return 0

    if len(li) == 2:
        return li[1] - li[0]

    p1 = 0
    p2 = 1
    max_ = li[p1] - li[p2]
    while p2 < len(li):
        while p2 < len(li) and li[p1] > li[p2]:  # 由于p2 > p2 所以p2减去后面的值肯定比p1减去后面的值大
            if li[p1] - li[p2] > max_ :
                max_ = li[p1] - li[p2]
            p2 += 1
        p1 = p2
        p2 += 1
    return max_

li = [9,1,7,18,6,20,17]
print(f(li))


