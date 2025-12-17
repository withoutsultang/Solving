import sys
def input(): return sys.stdin.readline()

stack = []

n = int(input())

for i in range(n):
    inst = input().strip()
    if len(inst) != 1:
        inst = list(map(int, inst.split()))
        if inst[0] == 1:
            stack.append(inst[1])
    else:
        inst = int(inst)
        if inst == 2:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif inst == 3:
            print(len(stack))
        elif inst == 4:
            print(0 if len(stack) else 1)
        elif inst == 5:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])