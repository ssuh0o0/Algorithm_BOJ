from collections import deque
n, k = map(int, input().split())
yQueue = deque([i+1 for i in range(n)])
print('<', end='')
while yQueue:
    cnt = 0
    for i in range(k-1):
        yQueue.append(yQueue.popleft())
    print(yQueue.popleft(), end='')
    if len(yQueue) != 0:
        print(', ', end='')
print('>', end='')
