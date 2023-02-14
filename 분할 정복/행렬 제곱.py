import sys
input = sys.stdin.readline

A = []
N, B = map(int, input().split())
for _ in range(N):
    A.append(list(map(int, input().split())))

def mulMatrix(a, b):
    tmp = [[0 for _ in range(len(a))] for _ in range(len(a))] 
    for i in range(len(a)):
        for j in range(len(a)):
            for l in range(len(a)):
                tmp[i][j] += a[i][l] * b[l][j] % 1000
    return tmp

def matrix(a, b):
    if b == 1:
        return a

    mat = matrix(a, b//2)

    if b % 2 :
        return mulMatrix(mulMatrix(mat, mat), A)
    else:
        return mulMatrix(mat, mat)

answer = matrix(A, B)
for ans in answer:
    for a in ans:
        print(a%1000, end=' ')
    print()