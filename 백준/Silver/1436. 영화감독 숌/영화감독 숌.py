import sys
def input(): return sys.stdin.readline()

n = int(input())
i = 666
count = 0
while(True):
    if('666' in str(i)):
        count += 1
        if count == n:
            print(i)
            break
    i += 1
