import sys
from collections import deque
def input(): return sys.stdin.readline()

m,n=map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]


q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((j,i))

while q:
    cx, cy = q.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
            graph[ny][nx] = graph[cy][cx] + 1
            q.append((nx,ny))

result = 0

for row in graph:
    if 0 in row:
        print(-1)
        exit()
    else:
        result = max(result, max(row))

    
print(result-1)

