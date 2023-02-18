#1912
import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))
num = dp[0]
for i in range(1, n):
    dp[i] = max(dp[i], dp[i] + dp[i-1])
    if num <= dp[i]:
        num = dp[i]
print(num)
