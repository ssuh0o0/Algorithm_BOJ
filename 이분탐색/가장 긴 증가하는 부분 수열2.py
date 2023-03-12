import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))

def binary_search(nlist, num):
    start, end = 0, len(nlist)-1

    while start <= end:
        mid = (start + end)//2
        if num > nlist[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start

num_list = [nlist[0]]
for n in range(1, len(nlist)):
    start = binary_search(num_list, nlist[n])
    if start >= len(num_list):
        num_list.append(nlist[n])
    else:
        num_list[start] = nlist[n]

print(len(num_list))