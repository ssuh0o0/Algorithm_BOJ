import sys
n, k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
sums = [0]
arrSum = 0
for i in range(n):
    arrSum += arr[i]
    sums.append(arrSum)

maxSum = -100 * k
for i in range(n-k+1):
    maxs = sums[i+k] - sums[i]
    if maxSum < maxs:
        maxSum = maxs
print(maxSum)
