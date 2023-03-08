import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))
bag = []
for _ in range(n):
    bag.append(list(map(int, input().split())))

dp = [[0] * (k+1) for _ in range(n+1)] 

for i in range(1, n+1):
    for j in range(1, k+1):   
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1]) 
        if j >= bag[i-1][0]:
            dp[i][j] = max(dp[i][j], dp[i-1][j - bag[i-1][0]] + bag[i-1][1])
            
print(dp[n][k])
