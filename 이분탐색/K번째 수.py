import sys
input = sys.stdin.readline
n = int(input())
k = int(input())

start = 1
end = k

answer = 0
while start <= end:
    cnt = 0
    mid = ( start + end )//2
    
    for i in range(1, n+1):
        cnt +=  min(mid//i, n)
    
    if cnt < k :
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
print(answer)