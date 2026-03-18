import sys
def input(): return sys.stdin.readline()

p = int(input())

for i in range(p):
    arr = list(map(int,input().split()))
    t = arr[0]
    count = 0
    for j in range(2,21):
        for q in range(1,j):
            if arr[j] < arr[q]:
                count += 1

    print(t,count)