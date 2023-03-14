import sys
input = sys.stdin.readline
n = int(input())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if nlist[i][0] + i > n: 
        dp[i] = dp[i+1]
    else: 
        dp[i] = max(dp[i+1], dp[i+nlist[i][0]] + nlist[i][1])
        
print(dp[0])  


