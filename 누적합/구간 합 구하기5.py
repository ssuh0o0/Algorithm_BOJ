import sys
n, m = map(int,sys.stdin.readline().split())
arr = [[0]*(n+1)]
for _ in range(n):
    arr.append([0]+list(map(int,sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, n):
        arr[i][j+1] += arr[i][j]

for j in range(1, n+1):
    for i in range(1, n):
        arr[i+1][j] += arr[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    a = arr[x2][y2]
    b = arr[x2][y1-1]
    c = arr[x1-1][y2]
    d = arr[x1-1][y1-1]
    print(a-b-c+d)
