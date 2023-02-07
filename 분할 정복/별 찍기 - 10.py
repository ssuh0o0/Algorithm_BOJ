import sys
input = sys.stdin.readline
n = int(input())


def countingStart(row, col, num):
    if row // num % 3 == 1 and col // num % 3 == 1:
        print(" ", end="")
    elif num // 3 == 0:
        print("*", end="")
    else:
        countingStart(row, col, num//3)

for i in range(n):
    for j in range(n):
        countingStart(i, j, n)
    print()
