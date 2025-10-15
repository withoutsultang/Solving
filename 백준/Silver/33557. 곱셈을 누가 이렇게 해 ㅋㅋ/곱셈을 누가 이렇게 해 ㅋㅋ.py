import sys

def input(): return sys.stdin.readline().rstrip()

n = int(input())
output = []

for _ in range(n):
    a, b = input().split()
    list_a = [int(d) for d in a]
    list_b = [int(d) for d in b]

    aCount = len(list_a)
    bCount = len(list_b)

    count = aCount if(aCount<bCount) else bCount

    for i in range(count):
        p = list_a.pop()
        q = list_b.pop()
        output.append(str(p*q))
    
    if(aCount>bCount):
        for d in reversed(list_a):
            output.append(str(d))
    else:
        for d in reversed(list_b):
            output.append(str(d))
    output.reverse()
    result = int("".join(output))
    answer = 1 if(result == (int(a) * int(b))) else 0
    print(answer)
    output = []


