import sys
input = sys.stdin.readline
n = int(input())
paperList = []
for _ in range(n):
    paperList.append(list(map(int, input().split())))

one = 0
zero = 0
minus = 0
def isFilled(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paperList[i][j] != paperList[x][y]:
                return False
    return True


def cutPaper(x, y, n):
    global one,zero,minus
    if n == 1 or isFilled(x,y,n):
        if paperList[x][y] == -1:
            minus += 1
        elif paperList[x][y]:
            one += 1
        else:
            zero += 1
        return

    n//=3
    dx = [x,x,x,x+n,x+n,x+n,x+2*n,x+2*n,x+2*n]
    dy = [y,y+n,y+2*n,y,y+n,y+2*n,y,y+n,y+2*n]

    for i in range(9):
        cutPaper(dx[i], dy[i], n)

cutPaper(0,0,n)
print(minus)
print(zero)
print(one)
