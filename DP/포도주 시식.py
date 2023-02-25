import sys
input = sys.stdin.readline
n = int(input())
wines = []
dp = [ 0 for _ in range(n)]
for _ in range(n):
    wines.append(int(input()))

if n >= 3:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(dp[1], max(wines[0], wines[1]) + wines[2])

    for i in range(3, n):
        dp[i] = max(dp[i-1], wines[i] + max(dp[i-3]+wines[i-1], dp[i-2]))
    print(max(dp))
else:
    print(sum(wines))
