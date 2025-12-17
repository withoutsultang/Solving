import sys
def input(): return sys.stdin.readline()

stack = []
result = 0

for ch in input().strip():
    if ch == '(':
        stack.append(ch)
    else:
        stack.pop()
        if pre == '(':
            result += len(stack)
        else:
            result += 1
    pre = ch

print(result)


