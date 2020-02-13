#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-3/challenges/cihat-needs-your-help
import sys
import heapq
from math import inf
sys.setrecursionlimit(1_000_000)

n, m = [int(x) for x in input().split()]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, w = [int(x) for x in input().split()]
    graph[x].append([w, y])
    graph[y].append([w, x])
start = 1

visited = [[False, False] for _ in range(n+1)]
distances = [[inf, inf] for _ in range(n+1)]
que = []

# 0 cost ile start'a gittim Gucumu kullanmadim
heapq.heappush(que, [0, start, 0])
distances[start][0] = 0

while que:
    cost, cur_node, is_used = heapq.heappop(que)

    if visited[cur_node][is_used]:
        continue
    visited[cur_node][is_used] = True

    for neig in graph[cur_node]:
        w, next_node = neig
        # daha kisa bi yol bulduysa!!!!
        if is_used:
            if cost + w < distances[next_node][1]:
                distances[next_node][1] = cost + w
                heapq.heappush(que, [distances[next_node][1], next_node, 1])

        else:
            # kullandigim case
            if cost + w//2 < distances[next_node][1]:
                distances[next_node][1] = cost + w//2
                heapq.heappush(que, [distances[next_node][1], next_node, 1])

            # kullanmadigim case
            if cost+w < distances[next_node][0]:
                distances[next_node][0] = cost + w
                heapq.heappush(que, [distances[next_node][0], next_node, 0])

print("-1" if distances[-1][1] == inf else distances[-1][1])