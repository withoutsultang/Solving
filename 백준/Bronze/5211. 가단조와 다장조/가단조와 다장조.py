import sys
def input(): return sys.stdin.readline()

danjo = 0
jangjo = 0

d = ('A', 'D', 'E')
j = ('C', 'F', 'G')

sound = input().strip().split("|")

for i in sound:
    if i[0] in d:
        danjo += 1
    elif i[0] in j:
        jangjo += 1

if danjo == jangjo:
        if sound[-1][-1] in d:
            danjo += 1
        elif sound[-1][-1]  in j:
            jangjo += 1


print("C-major" if jangjo>danjo else "A-minor")