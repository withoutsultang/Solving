import sys
def input(): return sys.stdin.readline()

n,m = map(int, input().split())

nb = [0] * m
op = []

def dfs(depth):
    if depth == m: 
        op.append(' '.join(map(str,nb)))
        return


    for i in range(1, n+1):
            nb[depth] = i
            dfs(depth+1)


dfs(0)
print('\n'.join(op))
