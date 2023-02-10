import sys
input = sys.stdin.readline
n = int(input())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().split())))

white = 0
blue = 0

def isFilled(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if nlist[i][j] != nlist[x][y]:
                return False
    return True

def countWhiteOrBlue(x, y, n):
    global white, blue
    
    if n == 1 or isFilled(x, y, n):
        if nlist[x][y]: 
            blue += 1
            return
        else: 
            white += 1
            return

    n //= 2
    dx = [x, x + n, x, x + n]
    dy = [y, y, y + n, y + n]

    for i in range(4):
       countWhiteOrBlue(dx[i], dy[i], n)


countWhiteOrBlue(0,0,n)
print(white)
print(blue)

 


