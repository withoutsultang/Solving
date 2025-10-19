import sys
def input(): return sys.stdin.readline()

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    c = a*b

    while(b!=0):
        a, b = b, a%b

    result = c // a
    print(result) 