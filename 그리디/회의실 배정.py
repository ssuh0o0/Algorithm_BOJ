import sys

n = int(sys.stdin.readline())
cnt = 1
time =[]
for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))
time = sorted(time, reverse=True)

cmpTime = time[0][0]
for i in range(1,n):
    if time[i][1] <= cmpTime:
        cnt += 1
        cmpTime = time[i][0]

print(cnt)