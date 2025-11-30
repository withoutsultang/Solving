import sys
def input(): return sys.stdin.readline()

while True:
    line = input().strip()
    if not line:
        break
    print(line)
    