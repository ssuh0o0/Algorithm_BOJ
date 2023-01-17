from collections import deque
num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    priority = deque(map(int, input().split()))
    idxs = deque([i+1 for i in range(n)])
    maxPrio = max(priority)
    cnt = 1
    while priority:
        p = priority.popleft()
        i = idxs.popleft()
        if p == maxPrio:
            if i-1 == m:
                print(cnt)
                break
            cnt += 1
            maxPrio = max(priority) 
        else:
            priority.append(p)
            idxs.append(i)


    