import sys
input = sys.stdin.readline
n = int(input())

cnt = 0
col = [0] * n

def Promising(nq):
    for i in range(nq):
        if col[nq] == col[i] or abs(col[nq] - col[i]) == (nq - i):
            return False
    return True

def n_queens(nq):
    global cnt
    if Promising(nq):
        if nq == n:
            cnt += 1
            return
        else:
            for i in range(n):
                col[nq] = i
                n_queens(nq+1)

n_queens(0)
print(cnt)



