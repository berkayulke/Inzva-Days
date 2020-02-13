#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-1/challenges/it-is-brute-force
from math import inf
def permuts(arr):
    n = len(arr)
    lim = 2**n
    res = []
    for i in range(1, (int)(lim)):
        sub = []
        for j in range(0, n):
            if (i & (1 << j)):
                sub.append(arr[j])
        res.append(sub)
    return res

siz = int(input())
ar = [int(x) for x in input().split()]

subs = permuts(ar)

closest = inf
for sub in subs:
    s = abs(sum(sub))
    if s < closest:
        closest = s
print(closest)

