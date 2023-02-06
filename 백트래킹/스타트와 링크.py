#14889
import sys
input = sys.stdin.readline

n = int(input())
startlink = []
for _ in range(n):
    startlink.append(list(map(int, input().split())))
cmpN = 1000
start, link = 0, 0
visited= [False]*n
cnt = 0 
def dfs(count, idx):
    global cmpN, cnt 
    start, link = 0, 0
    if count == n//2: 
        for i in range(n):
            for j in range(i+1, n):
                if not visited[i] and not visited[j]:
                    start += startlink[i][j]
                    start += startlink[j][i]
                elif visited[i] and visited[j]:
                    link += startlink[i][j]
                    link += startlink[j][i]
        if cmpN > abs(start-link):
            cmpN = abs(start-link)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(count+1, i+1)
            visited[i] = False
            
        if cmpN == 0:
            return 
        
dfs(0,0)
print(cmpN)