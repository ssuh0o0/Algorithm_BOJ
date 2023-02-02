#15649
import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
nlist = []
visited = [False] * (n+1)
def dfs():
    if len(nlist) == m:
        print(' '.join(map(str, nlist)))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        nlist.append(i)
        visited[i] = True
        dfs()
        nlist.pop()
        visited[i] = False

dfs()