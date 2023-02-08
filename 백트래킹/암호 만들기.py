import sys
input= sys.stdin.readline
l, s = map(int, input().split())
alist = list(map(str, input().split()))
alist = sorted(alist)
vo = ['a', 'e', 'o', 'u', 'i']
voCount = 0
consCount = 0

def dfs(arr, count, idx):
    global voCount, consCount
    if count == l and voCount > 0 and consCount > 1:
        print(''.join(arr))
    
    for i in range(idx, s):
        if alist[i] in vo:
            voCount += 1
        else:
            consCount += 1
        arr.append(alist[i])      
        dfs(arr, count+1, i+1)
        if arr.pop() in vo:
            voCount -= 1
        else:
            consCount -= 1

dfs([], 0, 0)