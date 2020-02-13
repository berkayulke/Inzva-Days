#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-3/challenges/ecem-wants-to-go-home
import heapq
from math import inf

n, m = [int(x) for x in input().split()]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, w = [int(x) for x in input().split()]
    graph[x].append([w, y])
    graph[y].append([w, x])

start, end = [int(x) for x in input().split()]




visited = [False for _ in range(n+1)]
distances = [inf for _ in range(n+1)]
que = []

# 0 cost ile start'a gittim
heapq.heappush(que, [0, start])
distances[start] = 0

while que:
    cost, cur_node = heapq.heappop(que)
    if visited[cur_node]:
        continue
    visited[cur_node] = True

    for neig in graph[cur_node]:
        w, next_node = neig
        #daha kisa bi yol bulduysa!!!!
        if cost + w < distances[next_node]:
            distances[next_node] = cost + w
            heapq.heappush(que, [distances[next_node], next_node])

res = distances[end]
if res == inf:
    print(-1)
else:
    print(res)
