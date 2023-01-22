# O(n^2)의 시간을 돌아서 시간초과 코드

import sys
n, m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
sums = [0] * n
sums[0] = arr[0]
for idx in range(1,n):
    sums[idx] = sums[idx-1] + arr[idx]

cnt = 0
for i in range(n):
    for j in range(i,n):
        if (sums[j] - sums[i]) % m :
            cnt += 1
print(cnt)
