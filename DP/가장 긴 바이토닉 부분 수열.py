import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp1 = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]
for i in range(1, n):
    num1 = 0  
    for j in range(0, i):
        if a[i] > a[j] and num1 < dp1[j]:
            num1 = dp1[j]
            dp1[i] = num1 + 1

for i in range(n-2, -1, -1):
    num2 = 0
    for j in range(n-1, i ,-1):
        if a[i] > a[j] and num2 < dp2[j]:
            num2 = dp2[j]
            dp2[i] = num2 + 1

max = 0
for i in range(n):
    if dp1[i] + dp2[i] > max:
        max = dp1[i] + dp2[i]

print(max-1)