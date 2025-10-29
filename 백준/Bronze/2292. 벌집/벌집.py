import sys
def input(): return sys.stdin.readline()

n = int(input())
count = 1
honeycomb = 1

while(n > honeycomb):
    honeycomb += 6 * count
    count += 1


print(count)
    

