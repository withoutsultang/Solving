import sys
def input(): return sys.stdin.readline()

from collections import deque

n,k=map(int,input().split())
que = deque(range(1, n+1))
answer = []

while que:
    for _ in range(k-1):
        que.append(que.popleft())
    answer.append(que.popleft())

print("<" + ', '.join(map(str,answer)) + ">")
    
