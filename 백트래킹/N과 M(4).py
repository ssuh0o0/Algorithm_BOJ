#15652
import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
nlist = []
idx = 1
def dfs(idx):
    if len(nlist) == m:
        print(' '.join(map(str, nlist)))
        return

    for i in range(idx, n+1):
        nlist.append(i)
        dfs(i)
        nlist.pop()

dfs(idx)