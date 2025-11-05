import sys
def input(): return sys.stdin.readline()


n = 9
c = 1
r = 1
maximum = -1

for i in range(9):
    num = list(map(int,input().split()))

    if(maximum < max(num)):
        maximum = max(num)
        r = i + 1
        c = num.index(maximum) + 1

print(f"{maximum}\n{r} {c}")