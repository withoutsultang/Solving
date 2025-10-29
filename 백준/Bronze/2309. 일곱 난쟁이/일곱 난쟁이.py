import sys
def input(): return sys.stdin.readline()
shorter = []

for _ in range(9):
    shorter.append(int(input()))

shorter.sort()

check = False
sum_short = sum(shorter)


for i in range(len(shorter)):
    for j in range(i+1, len(shorter)):
        if (sum_short - shorter[i] - shorter[j]) == 100:
            for n in shorter:
                if n == shorter[i] or n == shorter[j]:
                    continue
                print(n)
            check = True
            break
    if check:
        break
# from itertools import combinations

# for c in combinations(shorter, 7):
#     if sum(c) == 100:
#         c = sorted(c)
#         for p in c:
#             print(p)

