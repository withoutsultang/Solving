import sys
def input(): return sys.stdin.readline()

n = int(input())
count = 0

for _ in range(n):
    ch = ''
    check_list = []
    check = True
    word = input()
    for c in word:
        if ch == c:
            continue
        elif c in check_list:
            check = False
            break
        ch = c
        check_list.append(ch)
    if check: count += 1

print(count)


