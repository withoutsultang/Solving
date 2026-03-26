import sys
from collections import deque
def input(): return sys.stdin.readline()

n,m=map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        cx,cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < m and 0<= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = graph[cy][cx] + 1
                q.append((nx,ny))       

bfs(0,0)
print(graph[n-1][m-1])



