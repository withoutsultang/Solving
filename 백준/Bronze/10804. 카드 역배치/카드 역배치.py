import sys
def input(): return sys.stdin.readline()

arr = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

for _ in range(10):
    a,b = map(int,input().split())

    temp = arr[a-1:b]

    temp = reversed(temp)

    arr[a-1:b] = temp

print(" ".join(arr))


