import sys
input = sys.stdin.readline
n = int(input())
nlist = [0] + list(map(int, input().split()))
for idx in range(1, len(nlist)):
    nlist[idx] += nlist[idx-1]
m = int(input()) 
for _ in range(m):
    i, j = map(int, input().split())
    print(nlist[j] - nlist[i-1])
