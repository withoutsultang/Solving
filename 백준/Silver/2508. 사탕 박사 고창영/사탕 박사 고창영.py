import sys
def input(): return sys.stdin.readline()

n = int(input())

for _ in range(n):
    case = []
    count = 0

    line = input().strip()
    while not line:
        line = input().strip()

    r,c = map(int,line.split())

    for _ in range(r):
        a = input().strip()
        count += a.count('>o<')
        case.append(list(a))
    for i in range(c):
        cross = ''
        for j in range(r):
            cross += case[j][i]
        count += cross.count('vo^')
    print(count)
