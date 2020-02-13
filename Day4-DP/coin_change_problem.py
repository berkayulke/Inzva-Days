#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-4/challenges/coin-change
from sys import setrecursionlimit
setrecursionlimit(10_000)

target, coin_amount = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]

dp = [1_005*[-1] for _ in range(1_005)]

def f(ind, tar):
    if tar < 0:
        return 0

    if ind == coin_amount:
        if tar == 0:
            return 1
        return 0
    
    if dp[ind][tar] != -1:
        return dp[ind][tar]

    dp[ind][tar] = f(ind+1, tar) + f(ind, tar-coins[ind])
    return dp[ind][tar]

print(f(0,target))