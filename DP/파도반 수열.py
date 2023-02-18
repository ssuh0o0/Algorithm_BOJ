#9461
import sys
input = sys.stdin.readline

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + ([0] * 91)

n = int(input())
max = 10
for _ in range(n):
    num = int(input())

    for i in range(max, num+1):
        dp[i] = dp[i-1] + dp[i-5]
        max = num
    
    print(dp[num-1])

