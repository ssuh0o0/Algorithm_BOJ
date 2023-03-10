import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
nlist = []
for _ in range(n):
    nlist.append(input())

cnt = 0
for i in range(m):
    word = input()
    if word in nlist:
        cnt += 1

print(cnt)