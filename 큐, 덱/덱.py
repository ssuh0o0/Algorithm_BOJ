import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deq = deque()

for _ in range(n):
    string = input().split()

    if len(string)>1:
        st, num = string[0], int(string[1])
    else:
        st = string[0]

    if st == 'push_back':
        deq.append(num)
    elif st == 'push_front':
        deq.appendleft(num)
    elif st == 'pop_front':
        print(deq.popleft()) if deq else print(-1)
    elif st == 'pop_back':
        print(deq.pop()) if deq else print(-1)
    elif st == 'size':
        print(len(deq))
    elif st == 'empty':
        print(0) if deq else print(1)
    elif st == 'front':
        print(deq[0]) if deq else print(-1)
    elif st == 'back':
        print(deq[-1]) if deq else print(-1)
