import sys
def input(): return sys.stdin.readline()

n = int(input())

candy = input().strip().split()

candy_list = dict()

result = True

for c in candy:
    if c in candy_list.keys():
        candy_list[c] += 1
    else:
        candy_list[c] = 1

for c in candy_list.values():
    if c >= 3:
        result = False

print("Yes" if result else "No")
