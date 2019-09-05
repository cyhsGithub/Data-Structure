import copy
s = 'abc'

ans = []
depth = 0
def permuation(s, pos):
    global ans

    if s == []:
        return
    if len(s[pos:]) == 1:
        ans.append(copy.copy(s))
        return

    repeated = []
    for i in range(pos, len(s)):
        if s[i] not in repeated:
            repeated.append(s[i])
            s[pos], s[i] = s[i], s[pos]

            permuation(s, pos+1)

            s[pos], s[i] = s[i], s[pos]

s = list(s)
permuation(s, 0)
print([''.join(i) for i in ans])
