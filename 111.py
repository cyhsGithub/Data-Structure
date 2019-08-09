def f(li, s):
    if li == [] or len(li) == 1:
        return False

    dic = {}
    ans = []
    for i,v in enumerate(li):
        if v not in dic.keys():
            dic.update({v:[i]})
        else:
            dic[v].append(i)

        if s - v in dic.keys():
            for n in dic[s-v]:
                ans.append((dic[v][-1], n))

    return ans
l = [9, 1, 7, -1, 12, -1]
print(f(l, 8))