import sys
input = sys.stdin.readline

n = int(input())

def fibonacci(n):
    cnt2 = 0
    f = [ 0 for _ in range(n+1)]
    f[1] = f[2] = 1
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i-1] + f[i-2]
    return [f[n], cnt2]


print(fibonacci(n)[0],fibonacci(n)[1])
    