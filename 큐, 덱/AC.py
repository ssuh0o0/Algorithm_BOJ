from collections import deque

t =int(input())
for _ in range(t):
    p = input()
    n = int(input())
    deqX = input()
    if n > 0:
        deqX = deque(deqX[1:-1].split(','))
    else:
        deqX = deque()
    cnt = 0
    isNotD = True

    for p_str in p:
        if p_str == 'R':
            cnt += 1
        elif p_str == 'D':
            if deqX:
                if cnt % 2 == 1:
                    deqX.pop() 
                else:
                    deqX.popleft()
            else:
                print('error')
                isNotD = False
                break
             
    if isNotD:
        if cnt % 2 == 1:
            deqX.reverse()
        print("[" + ",".join(deqX) + "]")