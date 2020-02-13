#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-1/challenges/ugurs-dilemma/submissions/code/1319877907
k, q = [int(x) for x in input().split()]
libr = [int(x) for x in input().split()]
topics = [int(x) for x in input().split()]


def dif(a, b):
    return abs(a-b)

libr.sort()

def b_s(ar, val):
    if val > ar[-1]:
        return ar[-1]
    elif val < ar[0]:
        return ar[0]
    l, r, m = 0, len(ar)-1, (len(ar)-1)//2
    while l <= r:
        m = (l+r)//2
        if ar[m] == val:
            return ar[m]
        elif ar[m] > val:
            r = m-1
        else:
            l = m+1
    if dif(ar[l], val) > dif(ar[r], val):
        return ar[r]
    return ar[l]
for top in topics:
    closest = b_s(libr,top)
    print(dif(top,closest),end=" ")
