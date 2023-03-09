import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
nlist = list(map(int, input().split()))

start = 0
end = max(nlist)

def count(list, num):
    cnt = 0
    for l in list:
        if l > num :
            cnt += l - num
    return cnt

while start <= end:
    mid = (start + end) // 2
    cnt = count(nlist, mid)
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)