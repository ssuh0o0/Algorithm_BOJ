import sys
input = sys.stdin.readline
n = int(input())

dp = [0 for _ in range(n)]
stairs = [0 for _ in range(n)]
for i in range(n):
    stairs[i] = int(input())



if n >= 3:
    dp[0] = stairs[0]
    dp[1] = stairs[1] + stairs[0]
    dp[2] =  stairs[2] + max(stairs[1] , stairs[0])

    for i in range(3, n):
        dp[i] = stairs[i] + max(dp[i-3]+ stairs[i-1], dp[i-2])
    print(dp[-1])
else:
    print(sum(stairs))

