import sys
def input(): return sys.stdin.readline()

n = int(input())
count = 0

for i in range(n):
    sum = 0
    word = input()
    for c in word:
        if c == 'O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)
    


