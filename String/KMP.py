def gen_next(s):
    next = [0] * len(s)

    for i,v in enumerate(s):
        count = 0
        if i == 0:
            next[i] = 0
            continue

        new = s[:i+1]
        for n in range(len(new)//2):
            pre = new[:n+1]
            sub = new[-(n+1):]
            if pre == sub:
                count = (n+1)

        if i < len(s)-1:
            if s[i+1] == count:
                next[i] = next[count]
        else:
            next[i] = count

    #let next[-1] = -1
    next.append(-1)
    return next

def gen_next_(s):
    next = [0] * len(s)

    next[0] = -1
    j = 0
    k = -1

    while j < len(s)-1:
        if k == -1 or s[j] == s[k]:
            j += 1
            k += 1
            if s[j] == s[k]:
                next[j] = next[k]
            else:
                next[j] = k
        else:
            k = next[k]

    #let next[-1] = -1
    # next.append(-1)
    return next

def kmp(string, pattern):
    next = gen_next(pattern)
    print(next)
    j = 0
    i = 0
    while True:
        #match finished
        if j == len(pattern):
            print(i - j + 1)
            return

        #i move forward
        if j == -1 and string[i] != pattern[j]:
            i += 1
            j = 0

        #i,j move forward
        if string[i] == pattern[j]:
            j += 1
            i += 1
            continue

        j = next[j - 1]
        print(i,j)

string = "abadabadabaa"
pattern = "aaaaaa"
# kmp(string,pattern)
m = gen_next(pattern)
n = gen_next_(pattern)
print(m,n)