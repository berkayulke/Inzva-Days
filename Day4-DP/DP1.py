#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-4/challenges/salih-is-very-efficient
n,C = [int(x) for x in input().split()]

value = [0 for _ in range(n+2)]
weigth = [0 for _ in range(n+2)]

dp = [0 for _ in range(100000)]

for i in range(1,n+1):
    a,b = [int(x) for x in input().split()]
    value[i] = a
    weigth[i] = b

for i in reversed(range(1,n+1)):
    for c in reversed(range(weigth[i],C+1)):
        if c - weigth[i] >= 0:
            dp[c] = max(dp[c],dp[c - weigth[i]] + value[i])
print(dp[C])