import sys
def input(): return sys.stdin.readline()

a, b = map(int, input().split())

for i in range(1, a+1 if a>b else b+1):
    if(i == 1):
        print(f"{i} {a} {b}")
    elif a % i == 0 and b % i == 0:
        print(f"{i} {int(a/i)} {int(b/i)}")
