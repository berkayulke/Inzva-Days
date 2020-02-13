#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-4/challenges/it-is-not-lis
n = int(input())
ar = []
res = 0
for _ in range(n):
    ar.append(int(input()))

lis = [0 for _ in range(1_005)]
pre = [0 for _ in range(1_005)]

for i in range(0, n):
    mx = 0
    for j in range(0, i):
        if ar[i] > ar[j] and mx < lis[j]:
            mx = lis[j]
            pre[i] = j
    lis[i] = mx + 1
    if res < lis[i]:
        res = lis[i]

print(res)