import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nlist = list(map(int, input().split()))
cnt = 0

def dfs(arr, idx):
    global cnt

    # if idx >= n :
    #     return

    if arr and sum(arr) == s:
        cnt += 1

    for i in range(idx, n):
        arr.append(nlist[i])
        dfs(arr, i+1)
        arr.pop()

dfs([], 0)
print(cnt)

