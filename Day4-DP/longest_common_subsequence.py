#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-4/challenges/dynamic-programming-classics-the-longest-common-subsequence
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

dp = [105*[-1] for _ in range(105)]


def f(i, j):
    if i == n or j == m:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if a[i] == b[j]:
        dp[i][j] = 1 + f(i+1, j+1)
    else:
        dp[i][j] = max(f(i+1, j), f(i, j+1))

    return dp[i][j]


def yaz(i, j):
    if i == n or j == m:
        return 0

    if a[i] == b[j]:
        print(a[i], end=" ")
        yaz(i+1, j+1)
        return

    if dp[i][j] == dp[i][j+1]:
        yaz(i,j+1)
    else:
        yaz(i+1,j)


f(0, 0)
yaz(0,0)