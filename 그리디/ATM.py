#11399
import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
nlist = sorted(nlist)

for i in range(1,n):
    nlist[i] += nlist[i-1]

print(sum(nlist))