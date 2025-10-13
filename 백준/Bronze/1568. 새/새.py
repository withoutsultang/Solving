n = int(input())
count = 1
second = 0

while(True):
    if(n == 0):
        break
    if(n < count):
        count = 1
        continue
    n -= count
    second += 1
    count += 1

print(second)