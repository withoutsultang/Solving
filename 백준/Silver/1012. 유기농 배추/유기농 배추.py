import sys
from collections import deque
def input(): return sys.stdin.readline()

t = int(input())

def dfs(x,y):
    graph[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            graph[ny][nx] = 0
            dfs(nx,ny)

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[y][x] = 0

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx,ny))
            

dx = [0, 0, -1, 1] 
dy = [-1, 1, 0, 0]

for _ in range(t):
    m, n, k = map(int,input().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x,y=map(int,input().split())

        graph[y][x] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
                bfs(j,i)
    print(count)
    




