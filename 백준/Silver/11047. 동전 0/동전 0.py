import sys
def input(): return sys.stdin.readline()

n,k=map(int,input().split())

coin = [int(input()) for _ in range(n)]

count = 0

for i in reversed(coin):
    if k // i > 0:
        count += k // i
        k %= i

print(count)
