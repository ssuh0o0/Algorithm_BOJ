import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    num = 0
    for j in range(0, i):
        if nlist[i] > nlist[j] and num < dp[j]:
            num = dp[j]
            dp[i] = num + 1
    
print(max(dp))