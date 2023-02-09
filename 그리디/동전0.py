#11047
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)

cnt = 0

for i in range(len(coins)-1, -1,-1):
    if k == 0:
        break
    k, div = k % coins[i], k // coins[i]
    cnt += div

print(cnt)