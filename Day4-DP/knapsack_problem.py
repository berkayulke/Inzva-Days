#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-4/challenges/unbounded-knapsack/problem
t = int(input())

for _ in range(t):
    n,target = [int(x) for x in input().split()]
    coins = [int(x) for x in input().split()]
    
    #dp[i] = True demek i kadar coin toplayabiliyorum
    dp = (target+10000)*[False]
    dp[0] = True
    
    for coin in coins:
        dp[coin] = True
        for i in range(coin,target+1):
            if dp[i - coin] == True:
                dp[i] = True
    
    for j in reversed(range(target+1)):
        if dp[j] == True:
            print(j)
            break