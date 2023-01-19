import sys
n, m = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
psum = [0] * (n+1)
for idx in range(1,n+1):
    psum[idx] = psum[idx-1] + l[idx-1]
for _ in range(m):
    i, j = map(int,sys.stdin.readline().split())
    print(psum[j]-psum[i-1])
