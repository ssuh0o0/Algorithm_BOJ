#14888

import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
minN, maxN = 1000000000, -1000000000

def dfs(num , ans):
    global add, sub, mul, div, minN, maxN
    if num == n:
        if minN > ans:
            minN = ans      
        if maxN < ans:
            maxN = ans
        return
    else:
        if add > 0:
            add -= 1
            dfs(num+1, ans + nlist[num])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(num+1, ans - nlist[num])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(num+1, ans * nlist[num])
            mul += 1
        if div  > 0:
            div -= 1
            dfs(num+1, int(ans / nlist[num]))
            div += 1

dfs(1, nlist[0])
print(maxN)
print(minN)