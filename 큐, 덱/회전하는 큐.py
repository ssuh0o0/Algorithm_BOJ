from collections import deque
n, m = map(int, input().split())
nums = deque(map(int, input().split()))
idxs = deque([i+1 for i in range(n)])
cnt = 0
while m:
    num = nums.popleft()
    i = idxs.index(num)
    m -= 1
    if i == 0:
        idxs.popleft()
        continue
    elif i < len(idxs)/2:
        for j in range(len(idxs)//2 + 1):  
            
            out = idxs.popleft()         
            if out == num:
                break
            else:
                cnt += 1
                idxs.append(out)
    else:
        for j in range(len(idxs)-1, len(idxs)//2-1, -1):
            cnt += 1
            out = idxs.pop()
            if out == num:
                break
            else:
                
                idxs.appendleft(out)
print(cnt)