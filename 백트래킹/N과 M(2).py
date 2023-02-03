#15650
import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
nlist = []
visited = [False] * (n+1)
idx = 1
def dfs(idx):
    if len(nlist) == m:
        print(' '.join(map(str, nlist)))
        return

    for i in range(idx, n+1):
        if visited[i]:
            continue
        nlist.append(i)
        visited[i] = True
        dfs(i)
        nlist.pop()
        visited[i] = False

dfs(idx)