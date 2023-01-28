import sys
from collections import deque
n = int(sys.stdin.readline())
nQue = deque([i+1 for i in range(n)])
while len(nQue) > 1:
    nQue.popleft()
    nQue.append(nQue.popleft())

print(nQue[0])

