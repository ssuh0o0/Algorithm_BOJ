import sys
input = sys.stdin.readline

n = int(input())
I = [[1,1],[1,0]]

def fibonacci(a, b):
    tmp = [[0,0],[0,0]] 
    for i in range(2):
        for j in range(2):
            for l in range(2):
                tmp[i][j] += a[i][l] * b[l][j] % 1000000007
    return tmp

def matrix(mat, num):

    if num == 0: 
        return [[0,0],[0,0]] 

    if num == 1:
        return mat
    
    m = matrix(mat, num//2)

    if num % 2 :
        return fibonacci(fibonacci(m, m), mat)
    else:
        return fibonacci(m, m)

print(matrix(I, n)[0][1] % 1000000007)