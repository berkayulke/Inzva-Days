#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-2/challenges/degree-1
n,m= [int(x) for x in input().split()]
ar = n*[0]
for _ in range(0,m):
    u,v =[int(x) for x in input().split()]
    ar[u-1]+=1
    ar[v-1]+=1

for node in ar:
    print(node,end = " ")
