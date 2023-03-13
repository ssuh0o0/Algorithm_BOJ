import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if not num:
        if not len(heap):
            print(0)
        else:
            print(heappop(heap)[1])  
    else:
        heappush(heap, (-num, num))

