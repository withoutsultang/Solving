import sys
def input(): return sys.stdin.readline()

from collections import deque

deck = deque()

n = int(input())

for _ in range(n):
    inst = input().strip()
    if len(inst) != 1:
        inst = list(map(int, inst.split()))
        if inst[0] == 1:
            deck.appendleft(inst[1])
        elif inst[0] == 2:
            deck.append(inst[1])
    else:
        inst = int(inst)
        if inst == 3:
            if len(deck):
                print(deck.popleft())
            else:
                print(-1)
        elif inst == 4:
            if len(deck):
                print(deck.pop())
            else:
                print(-1)
        elif inst == 5:
            print(len(deck))
        elif inst == 6:
            print(1 if not deck else 0)
        elif inst == 7:
            print(-1 if not deck else deck[0])
        elif inst == 8:
            print(-1 if not deck else deck[-1])
