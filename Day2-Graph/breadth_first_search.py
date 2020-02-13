#https://www.hackerrank.com/contests/inzva-winter-camp-2020-day-2/challenges/what-does-kayacan-want/problem
n, m = [int(x) for x in input().split()]
adj_list = [[].copy() for _ in range(0, n+10)]

for _ in range(0, m):
    u, v = [int(x) for x in input().split()]
    adj_list[u].append(v)
    adj_list[v].append(u)
# adj_list ready

visited = [False for _ in range(0,n+1)]
visited[0] = True
cur_node = 1
queue = []
queue.append(cur_node)
visited[cur_node] = True  

while queue != []:
    cur_node = queue.pop(0)
    for child in adj_list[cur_node]:
        if visited[child] == False:
            queue.append(child)
            visited[child] = True
if False in visited:
    print("Not Connected")
else:
    print("Connected")
