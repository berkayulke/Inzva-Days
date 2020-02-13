#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-3/challenges/kruskalmstrsub
import sys
sys.setrecursionlimit(1_000_000)

g_nodes, g_edges = [int(x) for x in input().split()]

ancestor = [i for i in range(0, g_nodes+2000)]
edge_list = []

#weight_list = []
#points = []

weight = 0

def find(x):
    if x == ancestor[x]:
        return x
    ancestor[x] = find(ancestor[x])
    return ancestor[x]

for _ in range(g_edges):
    g_from, g_to, g_wei = [int(x) for x in input().split()]
    if g_from == g_to:
        continue
    edge_list.append([g_wei, g_from, g_to])

edge_list.sort()

for cost,x,y in edge_list:
    anc_x = find(x)
    anc_y = find(y)

    if anc_x == anc_y:
        continue
        
    weight += cost
    ancestor[anc_x] = anc_y 
print(weight)
