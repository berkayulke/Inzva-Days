#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-2/challenges/summer-camp
from string import ascii_lowercase
from collections import defaultdict
temp = defaultdict(lambda: 0)
results = defaultdict(lambda: temp.copy())

def possible_moves(x, y):
    res = []
    res.append([x+1, y+2])
    res.append([x+1, y-2])
    res.append([x-1, y+2])
    res.append([x-1, y-2])
    res.append([x+2, y+1])
    res.append([x+2, y-1])
    res.append([x-2, y+1])
    res.append([x-2, y-1])
    i = 0
    si = len(res)
    while i < si:
        cur = res[i]
        if cur[0] < 1 or cur[0] > 8 or cur[1] < 1 or cur[1] > 8:
            res.pop(i)
            i -= 1
            si -= 1
        i += 1
    return res


def place_to_index(place):
    f = ascii_lowercase.index(place[0]) + 1
    s = int(place[1])
    return [f, s]


t = int(input())

for _ in range(0, t):
    visited = [9*[False] for _ in range(0, 9)]
    distances = [9*[None] for _ in range(0, 9)]
    
    s, e = [x for x in input().split()]

    if results[s][e] != 0:
        print(f"To get from {s} to {e} takes {results[s][e]} knight moves.")
        continue
        
    
    start, end = place_to_index(s), place_to_index(e)
    res = 0

    que = []
    que.append(start)

    visited[start[0]][start[1]] = True
    distances[start[0]][start[1]] = 0
    while que:
        cur = que.pop(0)
        cur_dist = distances[cur[0]][cur[1]]
        if cur[0] == end[0] and cur[1] == end[1]:
            res = cur_dist
            break
        for po in possible_moves(cur[0], cur[1]):
            x, y = po[0], po[1]
            if visited[x][y] == False:
                visited[x][y] = True
                que.append([x, y])
                distances[x][y] = 1 + cur_dist
    print(f"To get from {s} to {e} takes {res} knight moves.")
    results[s][e] = res
    results[e][s] = res

