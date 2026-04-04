import sys
def input(): return sys.stdin.readline()

n = input().split('-')

for i in range(len(n)):
    n[i] = sum(map(int, n[i].split('+')))

result = n[0]

for i in range(1, len(n)):
    result -= n[i]

print(result)
