# O(n^2)의 시간을 돌아서 시간초과 코드
import sys
n, m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

aSum = 0
sums = [0] * m
for i in range(n):
    aSum += arr[i]
    sums[aSum%m] += 1

answer = sums[0]
for a in range(n):
    answer += a * (a-1) //2
print(answer)


