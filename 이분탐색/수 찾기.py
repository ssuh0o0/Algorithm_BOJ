import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

answer = [0 for _ in range(m)]
nlist.sort()
for i in range(m):
    start, end = 0, n-1
    while start <= end:
        mid = (start+end) // 2
        if nlist[mid] < mlist[i]:
            start = mid + 1
        elif nlist[mid] > mlist[i]:
            end = mid - 1
        else:
            answer[i] = 1
            break

for i in answer:
    print(i)


# import sys
# input = sys.stdin.readline
# n = int(input())
# nlist = set(map(int, input().split()))
# m = int(input())
# mlist = list(map(int, input().split()))

# for ml in mlist:				
#     print(1) if ml in nlist else print(0)

