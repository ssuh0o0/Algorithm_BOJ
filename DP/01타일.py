import sys
input = sys.stdin.readline


dp = [0]*1000001
dp[1]=1
dp[2]=2

for i in range(3 ,1000001):

    dp[i]=dp[i-1]+dp[i-2] 

    if dp[i] >= 15746: 
        dp[i] %= 15746 

print(dp[int(input())])