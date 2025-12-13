import sys
def input(): return sys.stdin.readline()

n = int(input())

for _ in range(n):
    m = int(input())
    word = [input().strip() for _ in range(m)]

    ans = None

    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            temp = word[i] + word[j]
            if temp == temp[::-1]:
                ans = temp
                break
        if ans is not None:
            break

    print(ans if ans is not None else 0)