import sys
from collections import deque
def input(): return sys.stdin.readline()

m,n,h = map(int, (input().split()))

graph = []
for _ in range(h):
    layer = []
    for _ in range(n):
        layer.append(list(map(int, input().split())))
    graph.append(layer)


mz,my,mx = (-1,1,0,0,0,0),(0,0,-1,1,0,0),(0,0,0,0,-1,1)

dq = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                dq.append((z,y,x))

while dq:
    z,y,x = dq.popleft()
    for i in range(6):
        tz,ty,tx=z+mz[i],y+my[i],x+mx[i] 
        if 0 <= tz < h and 0 <= ty < n and 0 <= tx < m:
            if graph[tz][ty][tx] == 0:
                graph[tz][ty][tx] = graph[z][y][x] + 1
                dq.append((tz,ty,tx))

answer = 0

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 0:
                print(-1)
                sys.exit(0)
            answer = max(answer, graph[z][y][x])
print(answer-1)

                
