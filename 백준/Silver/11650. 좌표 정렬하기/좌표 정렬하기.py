import sys
def input(): return sys.stdin.readline()

n = int(input())

num = []

for _ in range(n):
    num.append(list(map(int,input().split())))

num.sort()

for i in range(n):
    print(f"{num[i][0]} {num[i][1]}")

