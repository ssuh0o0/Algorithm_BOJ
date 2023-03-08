import sys
input = sys.stdin.readline
k, n = list(map(int, input().split()))
klist = []
for _ in range(k):
    klist.append(int(input()))

start = 1
end = max(klist)

def count(list, num):
    cnt = 0
    for l in list:
        cnt += l//num
    return cnt

while start <= end:
    mid = (start + end) // 2
    
    cnt = count(klist, mid)

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)