import sys
def input(): return sys.stdin.readline()

n = int(input())

chat = set()

cnt = 0

for _ in range(n):
    temp = input().strip()
    if temp == 'ENTER':
        cnt += len(chat)
        chat.clear()
    else:
        chat.add(temp)

cnt += len(chat)

print(cnt)
