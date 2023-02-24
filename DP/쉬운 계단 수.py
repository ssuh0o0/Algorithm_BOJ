import sys
input = sys.stdin.readline

dp = [[0,0,0,0,0,0,0,0,0,0], [0,1,1,1,1,1,1,1,1,1]]
n= int(input())
for i in range(2,n+1):
    dp.append([0,0,0,0,0,0,0,0,0,0])
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

print(sum(dp[n])% 1000000000)