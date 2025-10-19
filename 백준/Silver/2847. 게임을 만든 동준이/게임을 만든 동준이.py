import sys
def input(): return sys.stdin.readline()

n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))
list.reverse()

count = 0

for i in range(len(list)):
    if i == 0:
        continue
    if(list[i] >= list[i-1]):
        count += abs((list[i-1] - 1) - list[i])
        list[i] = list[i-1] -1

print(count)