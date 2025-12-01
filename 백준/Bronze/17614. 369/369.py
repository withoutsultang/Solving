import sys
def input(): return sys.stdin.readline()

a = int(input())

cnt = {}

for n in range(1, a+1):
    for i in list(str(n)):
        temp = i
        if temp == '3' or temp == '6' or temp == '9':
            if temp in cnt:
                cnt[temp] += 1
            else:
                cnt[temp] = 1
print(sum(cnt.values()))