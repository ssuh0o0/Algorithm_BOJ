#1932
import sys
input = sys.stdin.readline
n = int(input())
dp = [[0] *(n+1)] 
for i in range(n):
    arr = list(map(int, input().split()))
    dp.append([0]+ arr + [0] * (n-len(arr)))

for i in range(2, n+1):
    for j in range(1, i+1):
        dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[n]))
