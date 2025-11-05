import sys
def input(): return sys.stdin.readline()

n = int(input())
b = 1
for i in range(n,0,-1):
    print(' ' * (i-1) + '* ' * (b-1) + '*')
    b += 1