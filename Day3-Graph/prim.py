#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-3/challenges/primsmstsub
import heapq

n, m = [int(x) for x in input().split()]
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
que = []
tot = 0

for _ in range(m):
    x, y, w = [int(x) for x in input().split()]
    graph[x].append([w, y])
    graph[y].append([w, x])
    #tot += w
start = int(input())

# 0 cost ile -1'den 1'e gittim
heapq.heappush(que, [0, [-1, 1]])

while que:
    cost,pair = heapq.heappop(que)
    x,y = pair
    if visited[y]:
        continue
    visited[y] = True
    tot += cost
    for neig in graph[y]:
        w,next_node = neig
        if not visited[next_node]:
            heapq.heappush(que,[w,[y,next_node]])

print(tot)
