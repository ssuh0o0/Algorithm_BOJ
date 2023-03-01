import sys
input = sys.stdin.readline
n = int(input())
nlist = []
dp = [1 for _ in range(n)]
for _ in range(n):
    nlist.append(list(map(int, input().split())))

nlist.sort() 
for i in range(1, n):
    for j in range(0, i):
        if nlist[i][1] > nlist[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))
