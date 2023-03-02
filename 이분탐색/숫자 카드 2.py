import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
dict = {}
for i in nlist:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

answer = []
for i in mlist:
    if i in dict:
        answer.append(dict[i])
    else:
        answer.append(0)

print(*answer)