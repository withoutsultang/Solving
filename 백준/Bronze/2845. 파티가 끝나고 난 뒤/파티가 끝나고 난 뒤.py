import sys
def input(): return sys.stdin.readline()

l, p = map(int,input().split())
answer = []

for i in list(map(int, input().split())):
    answer.append(str(i - l*p))

print(' '.join(answer))