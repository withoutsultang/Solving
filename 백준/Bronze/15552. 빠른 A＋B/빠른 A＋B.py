import sys

def input(): return sys.stdin.readline().rstrip()

count = int(input())

for i in range(count):
    a,b = map(int, input().split(" "))
    print(a+b)