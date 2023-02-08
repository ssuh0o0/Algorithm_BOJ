import sys
input = sys.stdin.readline

while True:
    nlist = list(map(str, input().split()))
    n = len(nlist) - 1
    if nlist[0] == '0':
        break
    def dfs(arr, count, idx):

        if count == 6:
            print(' '.join(arr))
            return
        
        for i in range(idx, n+1):
            arr.append(nlist[i])
            dfs(arr,count+1, i+1)
            arr.pop()
        
    dfs([], 0, 1)
    print()

  

