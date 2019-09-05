#最长递增非连续子序列
li = [2,3,1,4,2,1,2]
opt = [1]

for i in range(1, len(li)):
    if li[i] >= li[i-1]:
        opt.append(opt[i-1] + 1)
    else:
        c = False
        if i == 1:
            opt.append(1)
        else:
            for n in range(i-2, -1,-1):
                # print(n)
                if li[n] <= li[i]:
                    opt.append(opt[n] + 1)
                    c = True
                    break
            if not c:
                opt.append(1)
print(max(opt))