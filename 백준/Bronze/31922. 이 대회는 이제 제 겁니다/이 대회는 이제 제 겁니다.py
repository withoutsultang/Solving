import sys
def input(): return sys.stdin.readline()

a,p,c = map(int,input().split())

print(a+c if a+c >= p else p)