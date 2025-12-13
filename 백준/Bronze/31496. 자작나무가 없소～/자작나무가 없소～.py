import sys
def input(): return sys.stdin.readline()

n, m = input().strip().split()

n = int(n)

dic = {}

result = 0

for _ in range(n):
    a,b = input().strip().split()
    b = int(b)

    dic[a] = b

for item in dic.keys():
    item_list = item.split("_")
    if m in item_list:
        result += dic[item]

print(result)