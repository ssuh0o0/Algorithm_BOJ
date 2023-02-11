import sys
input =  sys.stdin.readline
n = int(input())
quad = []
for _ in range(n): 
    quad.append(list(map(str, input().strip())))

answer = []
def isFilled(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if quad[i][j] != quad[x][y]:
                return False
    return True

def makeQuadTree(x, y, n):
    
    if n == 1 or isFilled(x, y, n):
        answer.append(quad[x][y])
        return

    n//=2
    answer.append("(")
    makeQuadTree(x, y, n)
    makeQuadTree(x, y+n, n)
    makeQuadTree(x+n, y, n)
    makeQuadTree(x+n, y+n, n)
    answer.append(")")

makeQuadTree(0,0,n)
print("".join(answer))