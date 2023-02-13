import sys
input = sys.stdin.readline

a, b = [], []
n, m = map(int, input().split())
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
for _ in range(m):
    b.append(list(map(int, input().split())))

c = [[0 for _ in range(k)] for _ in range(n)] 

for i in range(n):
    for j in range(k):
        for l in range(m):
            c[i][j] += a[i][l] * b[l][j]
        print(c[i][j], end=' ')
    print()

