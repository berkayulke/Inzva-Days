#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-1/challenges/arrow-1-1
from collections import defaultdict
n = int(input())
balls = [int(x) for x in input().split()]
res = n
size = n

dic = {}
dic = defaultdict(lambda:0,dic)
for i in range(0,n):
    dic[i] = 0

for i in reversed(range(0,n)):
    dic[ balls[i] ] += 1
    if dic[balls[i]-1] != 0:
        res-=1
        dic[balls[i]-1]-=1
        
print(res)
